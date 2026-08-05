# PVR-EC-O Contamination Report Template

Required artifacts:

- dataset_hash_manifest
- benchmark_hash_manifest
- source_repo_exclusion_list
- eval_task_overlap_scan
- n_gram_overlap_scan
- exact_file_hash_scan
- near_duplicate_code_scan
- commit_date_cutoff_check
- issue_text_overlap_check
- solution_patch_overlap_check

For coding tasks, exclude benchmark repos, forks, mirrors, issue text, PR patches, and generated solutions from training.

If contamination status is unknown, mark `CONTAMINATION_STATUS_UNKNOWN`. Unknown is not clean.

