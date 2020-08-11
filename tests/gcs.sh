# /bin/bash
bucket_name=$(cat ../config.yaml|grep 'bucket-name'|awk '{print $NF}'|xargs)
gsutil ls gs://$bucket_name
if [ $? -eq 0 ]
then
	echo "Test succeeded"
else
	echo "Test failed"
fi
