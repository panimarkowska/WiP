import boto3

s3 = bucket.resoruce('s3')
bucket = s3.Bucket('pisxx')

my_file = open('pslawek_test.txt', 'w+')
my_file.write('testowy teks')
my_file.close()

bucket.put_object(Key='omega/gamma/test.txt', Body=open('pslawek_test.txt', 'rb'))
    
