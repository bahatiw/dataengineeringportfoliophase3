import random
from faker import Faker
from confluent_kafka import Producer
import json
import time

# List of 42 counties in Kenya
counties = ['Mombasa', 'Kwale', 'Kilifi', 'Tana River', 'Lamu', 'Taita–Taveta', 'Garissa', 'Wajir', 'Mandera', 'Marsabit', 'Isiolo', 'Meru', 'Tharaka-Nithi', 'Embu', 'Kitui', 'Machakos', 'Makueni', 'Nyandarua', 'Nyeri', 'Kirinyaga', 'Murang\'a', 'Kiambu', 'Turkana', 'West Pokot', 'Samburu', 'Trans-Nzoia', 'Uasin Gishu', 'Elgeyo-Marakwet', 'Nandi', 'Baringo', 'Laikipia', 'Nakuru', 'Narok', 'Kajiado', 'Kericho', 'Bomet', 'Kakamega', 'Vihiga', 'Bungoma', 'Busia', 'Siaya', 'Kisumu']

# List of possible produce
produce_list = ['Maize', 'Beans', 'Rice', 'Wheat', 'Barley', 'Sorghum', 'Potatoes', 'Cabbages', 'Tomatoes', 'Onions', 'Carrots']

# Initialize Faker
fake = Faker()

def generate_data():
    # Randomly select a county
    county = random.choice(counties)

    # Randomly select a produce
    produce = random.choice(produce_list)

    # Generate a fake farmer name
    farmer_name = fake.name()

    # Generate a random quantity (in kg)
    quantity = random.randint(1, 100)

    return {
        'County': county,
        'Farmer Name': farmer_name,
        'Produce': produce,
        'Quantity (kg)': quantity
    }
# 
p = Producer({'bootstrap.servers': '172.34.0.19:9092'})
def delivery_report(err, msg):
    """ Called once for each message produced to indicate delivery result.
        Triggered by poll() or flush(). """
    if err is not None:
        print('Message delivery failed: {}'.format(err))
    else:
        print('Message delivered to {} [{}]'.format(msg.topic(), msg.partition()))

# Generate and print data for 10 farmers
k=0
l=0
while l<10 :    
    for _ in range(10):
        # Trigger any available delivery report callbacks from previous produce() calls
        p.poll(0)
        data = generate_data()
        p.produce('dataengineringportfolio',value=str(data), callback=delivery_report)
        l=4
    p.flush()
    time.sleep(10)
    

