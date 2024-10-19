from flask import Flask, request, jsonify
import boto3
from PIL import Image
from io import BytesIO

app = Flask(__name__)
s3 = boto3.client('s3')

def download_image_from_s3(bucket_name, image_key):
    obj = s3.get_object(Bucket=bucket_name, Key=image_key)
    return obj['Body'].read()

def resize_image(image_data, max_size=(800, 600)):
    image = Image.open(BytesIO(image_data))
    image.thumbnail(max_size)
    buffer = BytesIO()
    image.save(buffer, format="JPEG")
    buffer.seek(0)
    return buffer

def upload_image_to_s3(bucket_name, image_key, image_data):
    s3.put_object(Bucket=bucket_name, Key=image_key, Body=image_data, ContentType='image/jpeg')

@app.route('/reduce-image-size', methods=['POST'])
def reduce_image_size():
    data = request.get_json()
    bucket_name = data['bucket_name']
    image_key = data['image_key']
    new_image_key = data['new_image_key']
    max_size = tuple(data.get('max_size', (800, 600)))
    
    original_image = download_image_from_s3(bucket_name, image_key)
    resized_image = resize_image(original_image, max_size)
    upload_image_to_s3(bucket_name, new_image_key, resized_image)

    return jsonify({'message': 'Image resized and uploaded successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
