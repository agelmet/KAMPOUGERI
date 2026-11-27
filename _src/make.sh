#!/bin/bash
# KAMPOUGERI build: src → site (cloud paths). ./make.sh
set -e
K=/home/claude/kb; A=/home/claude/ac/.advon; D=bodynoesis.com
cd $K && python3 src/build.py
python3 $A/privacy/privacy_fix.py apply $K/site >/dev/null
python3 src/post.py $K/site
cd $K/site && python3 $A/favicon.py make $K/site assets/img/body-noesis-icon.svg --tile none >/dev/null && cd $K
python3 $A/seo_live.py fix $K/site $D
python3 $A/seo_rank.py en $K/site $D
python3 $A/ai_seo.py fix $K/site $D
python3 $A/seo_live.py schema $K/site
