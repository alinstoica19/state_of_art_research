#!/usr/bin/env bash
# Usage: tools/commit_sub.sh S3   -> update STATUS.md row, append decisions, commit and push
set -e
cd "$(dirname "$0")/.."
S="$1"
CSV=$(ls results/${S}_*.csv | grep -v unverified | head -1)
N=$(python3 -c "import csv,sys;print(sum(1 for _ in csv.DictReader(open('$CSV'))))")
U=$(python3 -c "import csv,sys;print(sum(1 for _ in csv.DictReader(open('results/${S}_unverified.csv'))))" 2>/dev/null || echo 0)
python3 - "$S" "$N" "$U" <<'PY'
import re,sys
s,n,u=sys.argv[1:]
t=open("STATUS.md").read()
t=re.sub(r"^(\| %s \|[^|]*\|) [^|]* \| [^|]* \|$"%s, r"\1 **done** | %s (+%s unverified) |"%(n,u), t, flags=re.M)
open("STATUS.md","w").write(t)
PY
if [ -f work/${S}_decisions.md ] && ! grep -q "^### ${S} " DECISIONS.md; then
  { echo; echo "### ${S} (subagent decisions)"; echo; cat work/${S}_decisions.md; } >> DECISIONS.md
fi
git add STATUS.md DECISIONS.md results/${S}_* work/${S}* 
git commit -qm "Phase 2: ${S} done (${N} verified, ${U} unverified)

Co-Authored-By: Claude Opus 5.5 <noreply@anthropic.com>
Claude-Session: https://claude.ai/code/session_01URMUJzANNXYDPEdQYSffNt"
for i in 0 2 4 8 16; do sleep $i; git push -u origin claude/5g-6g-literature-search-2lyo41 -q && break; done
echo "committed $S: $N verified, $U unverified"
