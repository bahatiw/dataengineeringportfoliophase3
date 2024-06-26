# dataengineringprojectv3
This project involves farmers country wide reporting on production. The aim of this is so that there is national data on how much production farmers managed to produce
# Build a real-time data backend for a data-intensive application

## Installation
install docker desktop manager  [https://www.docker.com/products/docker-desktop/).
```
clone the contents of git repository
git clone https://github.com/bahatiw/dataengineeringportfoliophase3.git
cd  dataengineeringporfolio-phase3

```

## Usage

```Docker compose.. Build and run the images
Docker compose build
Docker compose up

# Sample Output from Consumer container while inserting into Mongo DB
consumer-container-1  | {'County': 'Kajiado', 'Farmer Name': 'Deborah Smith', 'Produce': 'Barley', 'Quantity (kg)': 12}
consumer-container-1  | {'County': 'Siaya', 'Farmer Name': 'Troy Lopez', 'Produce': 'Beans', 'Quantity (kg)': 94}
consumer-container-1  | {'County': 'Laikipia', 'Farmer Name': 'Nathan Reyes', 'Produce': 'Wheat', 'Quantity (kg)': 95}
consumer-container-1  | {'County': 'Mandera', 'Farmer Name': 'Joanna Johnson', 'Produce': 'Beans', 'Quantity (kg)': 89}
consumer-container-1  | {'County': 'Tharaka-Nithi', 'Farmer Name': 'Daniel Tran', 'Produce': 'Barley', 'Quantity (kg)': 42}
consumer-container-1  | {'County': "Murang'a", 'Farmer Name': 'Todd Fritz', 'Produce': 'Sorghum', 'Quantity (kg)': 82}
consumer-container-1  | {'County': 'Kisumu', 'Farmer Name': 'Lisa Hatfield', 'Produce': 'Beans', 'Quantity (kg)': 58}
consumer-container-1  | {'County': 'West Pokot', 'Farmer Name': 'Zachary Stephens', 'Produce': 'Wheat', 'Quantity (kg)': 34}
consumer-container-1  | {'County': 'Kitui', 'Farmer Name': 'Alyssa Gallagher', 'Produce': 'Tomatoes', 'Quantity (kg)': 53}
consumer-container-1  | {'County': 'Kirinyaga', 'Farmer Name': 'Stephanie Chan', 'Produce': 'Sorghum', 'Quantity (kg)': 26}
consumer-container-1  | {'County': 'Vihiga', 'Farmer Name': 'Marilyn Dawson', 'Produce': 'Carrots', 'Quantity (kg)': 65}
consumer-container-1  | {'County': 'Embu', 'Farmer Name': 'Crystal Schultz', 'Produce': 'Barley', 'Quantity (kg)': 40}
consumer-container-1  | {'County': 'Turkana', 'Farmer Name': 'Rachel Garza', 'Produce': 'Maize', 'Quantity (kg)': 24}
consumer-container-1  | {'County': 'Samburu', 'Farmer Name': 'Megan Baker', 'Produce': 'Potatoes', 'Quantity (kg)': 10}
consumer-container-1  | {'County': 'Kakamega', 'Farmer Name': 'Calvin Forbes', 'Produce': 'Wheat', 'Quantity (kg)': 3}
consumer-container-1  | {'County': 'Uasin Gishu', 'Farmer Name': 'Jennifer Jimenez', 'Produce': 'Sorghum', 'Quantity (kg)': 97

# Sample output from Consumer-Spark container (Writes to Console)
consumer-spark-1      | -------------------------------------------
consumer-spark-1      | Batch: 14
consumer-spark-1      | -------------------------------------------
consumer-spark-1      | +----+------------+-------------------+--------+-------------+
consumer-spark-1      | | key|      County|        Farmer Name| Produce|Quantity (kg)|
consumer-spark-1      | +----+------------+-------------------+--------+-------------+
consumer-spark-1      | |NULL|     Baringo|Jennifer Williamson| Carrots|           11|
consumer-spark-1      | |NULL|       Kitui|  Jessica Gallagher| Sorghum|            4|
consumer-spark-1      | |NULL|     Samburu| Jennifer Maldonado|    Rice|           88|
consumer-spark-1      | |NULL|        Meru|       Julie Dennis|    Rice|           40|
consumer-spark-1      | |NULL|    Murang'a|      Vernon Waters|   Beans|           59|
consumer-spark-1      | |NULL|Taita–Taveta|       Lacey Gordon| Sorghum|           69|
consumer-spark-1      | |NULL|  West Pokot|       Thomas Riley|  Barley|           20|
consumer-spark-1      | |NULL|      Kilifi|         Amy French| Sorghum|           24|
consumer-spark-1      | |NULL|      Isiolo|     Margaret Solis|   Beans|           52|
consumer-spark-1      | |NULL|     Mandera|       Amanda Knapp|Tomatoes|           94|
consumer-spark-1      | +----+------------+-------------------+--------+-------------+

# Sample Output from Generator container to Apache Spark
```
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]
producer-1            | Message delivered to dataengineringportfolio [0]

## Contributing

Pull requests are welcome. 

## License