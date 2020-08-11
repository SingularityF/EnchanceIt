# /bin/bash
bucket_name=$(cat ../config.yaml|grep 'bucket-name'|awk '{print $NF}'|xargs)
echo "TEST_STRING" > test_file
gsutil cp test_file gs://$bucket_name
if [ $? -eq 0 ]
then
        echo "Test succeeded"
else
        echo "Test failed"
fi
rm test_file
