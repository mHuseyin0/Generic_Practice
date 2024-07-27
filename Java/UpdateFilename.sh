pattern="Main[0-9]_"

for f in /home/huseyin/Documents/Backup/Coding/MainPractices/src/*; do
    if [[ "$f" =~ $pattern ]]; then
        newFileName=${f:60}
        mv "$f" "Main0$newFileName"
    fi
done
