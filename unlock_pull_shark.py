import subprocess
import time
import os

def run_cmd(cmd, cwd=None):
    print(f"Running: {cmd}")
    res = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if res.returncode != 0:
        print(f"ERROR: {res.stderr}")
    else:
        print(f"SUCCESS: {res.stdout.strip()}")
    return res

profile_dir = os.getcwd()
print(f"Working Directory: {profile_dir}")

# Ensure we are inside Hubrisdog_profile and on main
run_cmd("git checkout main", cwd=profile_dir)
run_cmd("git pull", cwd=profile_dir)

for i in range(1, 3):
    branch_name = f"temp-pullshark-{i}"
    print(f"\n--- STARTING PR {i} ---")
    
    # 1. Checkout new branch
    run_cmd(f"git checkout -b {branch_name}", cwd=profile_dir)
    
    # 2. Modify dummy file
    dummy_file = os.path.join(profile_dir, "pullshark_dummy.txt")
    with open(dummy_file, "a") as f:
        f.write(f"Pull Shark trigger step {i} at {time.time()}\n")
        
    # 3. Commit
    run_cmd("git add pullshark_dummy.txt", cwd=profile_dir)
    run_cmd(f'git commit -m "Trigger Pull Shark achievement step {i}"', cwd=profile_dir)
    
    # 4. Push
    run_cmd(f"git push -u origin {branch_name}", cwd=profile_dir)
    
    # 5. Create PR using gh CLI
    # We add a sleep to ensure GitHub sees the pushed branch
    time.sleep(2)
    pr_cmd = f'gh pr create --title "Trigger Pull Shark {i}" --body "Automated PR to unlock the Pull Shark badge." --head {branch_name} --base main'
    run_cmd(pr_cmd, cwd=profile_dir)
    
    # 6. Merge PR
    time.sleep(2)
    # Use -m to merge, -d to delete branch on github, -y to auto-confirm
    merge_cmd = "gh pr merge --merge -d --admin -y"
    run_cmd(merge_cmd, cwd=profile_dir)
    
    # 7. Clean up local state
    run_cmd("git checkout main", cwd=profile_dir)
    run_cmd("git pull", cwd=profile_dir)
    run_cmd(f"git branch -D {branch_name}", cwd=profile_dir)

print("\n--- DONE ---")
