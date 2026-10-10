#!/usr/bin/env bash
# Usage: tools/commit_sb.sh C1|C2|C3|C45|GAP  -> mark category done in STATUS_SNOWBALL.md, commit and push its files
set -e
cd "$(dirname "$0")/.."
G="$1"
CSV=$(ls results/SB_${G}_*.csv | grep -v unverified | head -1)
N=$(python3 -c "import csv;print(sum(1 for _ in csv.DictReader(open('$CSV'))))")
U=$(python3 -c "import csv;print(sum(1 for _ in csv.DictReader(open('results/SB_${G}_unverified.csv'))))" 2>/dev/null || echo 0)
python3 - "$G" "$N" "$U" <<'PY'
import re,sys
g,n,u=sys.argv[1:]
lab={"C1":"C1","C2":"C2","C3":"C3","C45":"C4\\+C5","GAP":"Gap check"}[g]
t=open("STATUS_SNOWBALL.md").read()
t=re.sub(r"^\| (2 Select \+ verify )?%s \|.*$"%lab, lambda m: "| %s%s | **done**: %s verified (+%s unverified) |"%(m.group(1) or "", lab.replace("\\",""), n, u), t, flags=re.M)
open("STATUS_SNOWBALL.md","w").write(t)
PY
git add STATUS_SNOWBALL.md results/SB_${G}_* work/SB_${G}.jsonl work/snowball/ $( [ "$G" = GAP ] && echo GAP_CHECK.md )
git commit -qm "Snowball phase 2: ${G} done (${N} verified, ${U} unverified)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01EuAobfKW5w5JjWnVzhGf7K"
for i in 0 2 4 8 16; do sleep $i; git push -u origin claude/5g-6g-literature-search-2lyo41 -q && break; done
echo "committed $G: $N verified, $U unverified"
