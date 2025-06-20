# SMP Dataset: Similar Music Pair Dataset

## Overview

The SMP dataset contains 70 music piece pairs for plagiarism detection research. This is currently a sample-scale dataset designed to demonstrate our approach and methodology. Each pair includes original and comparison tracks with temporal segments marking similar parts.

## Dataset Structure

- **ori_title**: Original music piece title
- **comp_title**: Comparison music piece title  
- **ori_link**: YouTube link to original
- **comp_link**: YouTube link to comparison
- **relation**: Relationship type (`plag`, `plag_doubt`, `remake`)
- **ori_times**: Similarity timestamps in original (seconds)
- **comp_times**: Similarity timestamps in comparison (seconds)
- **pair_number**: Unique pair identifier


## Current Limitations

This dataset represents a small-scale sample collection. We hope that this dataset become larger in future, to enable more robust plagiarism detection research.

## Usage

Dataset includes 70 pairs across diverse genres and time periods. Multiple timestamp pairs may exist per music pair. YouTube links provide audio access for analysis.

---

*For academic research use.(Even for us! haha.. we can't use these datasets for commercial purpose..) Respect copyright laws when accessing audio content!* 
