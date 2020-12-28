from dotenv import load_dotenv
import os

load_dotenv()

config = {
  'AWS_BUCKET':os.getenv('AWS_BUCKET'),
  'AWS_ACCESS_KEY':os.getenv('AWS_ACCESS_KEY'),
  'AWS_SECRET_ACCESS_KEY': os.getenv('AWS_SECRET_ACCESS_KEY'),
  'AWS_SESSION_TOKEN':os.getenv('AWS_SESSION_TOKEN')
}