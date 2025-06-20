import os
import csv
import subprocess
import time
from concurrent.futures import ThreadPoolExecutor
import pandas as pd

def download_audio(row, output_dir):
    """Download audio from YouTube link and save it with appropriate name"""
    pair_number = row['pair_number']
    titles = [row['ori_title'], row['comp_title']]
    links = [row['ori_link'], row['comp_link']]
    
    # Create directory for this pair if it doesn't exist
    pair_dir = os.path.join(output_dir, str(pair_number))
    os.makedirs(pair_dir, exist_ok=True)
    
    for i, (title, link) in enumerate(zip(titles, links)):
        # Clean filename
        clean_title = ''.join(c if c.isalnum() or c in ' -_' else '_' for c in title)
        clean_title = clean_title.strip()
        output_file = os.path.join(pair_dir, f"{clean_title}.wav")
        
        # Skip if file already exists
        if os.path.exists(output_file):
            print(f"File already exists: {output_file}")
            continue
            
        try:
            print(f"Downloading: {title} from {link}")
            # Use yt-dlp to download audio in wav format
            cmd = [
                'yt-dlp',
                '-x',                        # Extract audio
                '--audio-format', 'wav',     # Convert to wav
                '--audio-quality', '0',      # Best quality
                '-o', output_file,           # Output filename
                link                         # YouTube URL
            ]
            
            # Execute the command
            subprocess.run(cmd, check=True)
            print(f"Successfully downloaded: {output_file}")
            
            # Sleep to avoid rate limiting
            time.sleep(1)
            
        except subprocess.CalledProcessError as e:
            print(f"Error downloading {title}: {e}")
        except Exception as e:
            print(f"Unexpected error with {title}: {e}")

def main():
    # Set paths
    csv_path = 'Final_dataset_pairs.csv'  # Replace with your actual CSV path
    output_dir = 'final_dataset'
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Read CSV file
    df = pd.read_csv(csv_path)
    
    # Get unique pairs to download
    unique_pairs = df.drop_duplicates(subset=['pair_number', 'ori_title', 'comp_title', 'ori_link', 'comp_link'])
    
    print(f"Starting downloads for {len(unique_pairs)} unique pairs ({len(unique_pairs)*2} songs)...")
    
    # Use ThreadPoolExecutor for parallel downloads (adjust max_workers as needed)
    with ThreadPoolExecutor(max_workers=3) as executor:
        for _, row in unique_pairs.iterrows():
            executor.submit(download_audio, row, output_dir)
    
    print("Download process completed!")

if __name__ == "__main__":
    main()