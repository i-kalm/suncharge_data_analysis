{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "d1cb0461-febe-4bf8-99d6-f0a91bf6410d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "316cbba4-3070-41d9-9e15-ed35dc11879f",
   "metadata": {},
   "outputs": [],
   "source": [
    "data_directory = \"C:\\\\Users\\\\irina\\\\Documents\\\\UH\\\\Vizualization in Data Science DL\\\\suncharge\\\\data\"\n",
    "files = os.listdir(data_directory)\n",
    "for file in files:\n",
    "    print(file)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "id": "f80d6b31-2606-48cc-875b-230f26933c12",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "All files have been processed.\n"
     ]
    }
   ],
   "source": [
    "# source_directory = data_directory\n",
    "# destination_directory = data_directory\n",
    "# # Make sure the destination directory exists\n",
    "# os.makedirs(data_directory, exist_ok=True)\n",
    "\n",
    "# # Loop through all files in the source directory\n",
    "# for filename in os.listdir(source_directory):\n",
    "#     if filename.endswith('.csv'):  # Check if the file is a CSV\n",
    "#         file_path = os.path.join(source_directory, filename)\n",
    "        \n",
    "#         # Read the CSV file into a DataFrame\n",
    "#         df = pd.read_csv(file_path)\n",
    "        \n",
    "#         # Check and remove the \"Unnamed: 0\" column if it exists\n",
    "#         if 'Unnamed: 0' in df.columns:\n",
    "#             df = df.drop('Unnamed: 0', axis=1)\n",
    "        \n",
    "#         # Write the DataFrame back to a new CSV file without the unwanted column\n",
    "#         destination_file_path = os.path.join(destination_directory, filename)\n",
    "#         df.to_csv(destination_file_path, index=False)  # Set index=False to avoid writing row numbers as a separate column\n",
    "\n",
    "# print(\"All files have been processed.\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 78,
   "id": "9cc74539-1f5f-4f46-8ac1-079d0ff0d05d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   Material                        Component                 Product Category  \\\n",
      "0  EVCB-001                              NaN              EV Car Battery - FP   \n",
      "1    BC-001                    Battery Cells                    Battery Cells   \n",
      "2   BMS-001  Battery Management System (BMS)  Battery Management System (BMS)   \n",
      "3    CF-001                     Cooling Fans        Thermal Management System   \n",
      "4    CF-002                     Cooling Fans        Thermal Management System   \n",
      "\n",
      "  Finished Product  \n",
      "0   EV Car Battery  \n",
      "1   EV Car Battery  \n",
      "2   EV Car Battery  \n",
      "3   EV Car Battery  \n",
      "4   EV Car Battery  \n",
      "(42, 4)\n"
     ]
    }
   ],
   "source": [
    "bom_file = os.path.join(data_directory, 'bom.csv')\n",
    "bom = pd.read_csv(bom_file)\n",
    "print(bom.head(5))\n",
    "print(bom.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 76,
   "id": "0f000cb2-bb05-4ab2-9ad2-1fabc8cf501c",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   CustomerCountry  PlantKey\n",
      "0          Belgium         4\n",
      "1          Croatia         6\n",
      "2   Czech Republic         5\n",
      "3          Denmark         8\n",
      "4          Estonia         8\n",
      "5          Finland         8\n",
      "6           France         6\n",
      "7          Germany         4\n",
      "8           Greece         5\n",
      "9          Hungary         5\n",
      "10           Italy         6\n",
      "11          Latvia         8\n",
      "12       Lithuania         8\n",
      "13     Netherlands         4\n",
      "14          Norway         8\n",
      "15          Poland         5\n",
      "16        Portugal         6\n",
      "17        Slovenia         6\n",
      "18           Spain         6\n",
      "19          Sweden         8\n",
      "20     Switzerland         6\n",
      "21  United Kingdom         7\n"
     ]
    }
   ],
   "source": [
    "cpr_file = os.path.join(data_directory, 'CustomerPlantRelation.csv')\n",
    "cpr = pd.read_csv(cpr_file)\n",
    "print(cpr)\n",
    "#print(cpr.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "id": "e5489a8f-c242-4133-8371-38a660eb5813",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   CustomerKey                CustomerName CustomerCountry CustomerCity  \\\n",
      "0            1             O'Hara-MacGyver         Germany      Hamburg   \n",
      "1            2  Smitham, Lind and Lindgren         Germany      München   \n",
      "\n",
      "  CustomerPostalCode     CustomerStreet  PlantKey  \n",
      "0              22041  36 Westport Court         4  \n",
      "1              81679   934 Shelley Lane         4  \n",
      "(1227, 7)\n"
     ]
    }
   ],
   "source": [
    "cust_file = os.path.join(data_directory, 'Customers.csv')\n",
    "cust = pd.read_csv(cust_file)\n",
    "print(cust.head(2))\n",
    "print(cust.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 64,
   "id": "a1b84dc0-19bb-4d64-a89e-1dc20a44ce8a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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3Lx5k+joaABWrVqlLnvz5k1MTU359NNPmTNnDleuXCEhIQFzc3OtgaDPkqSLFy8CsH79ehwdHbGzs8tWrC1btmTmzJnqGI2kpCTOnz+fYdnbt2+j0Who2bIl33//PYqiqONOXrRq1SpSU1N59OgRa9eupUGDBpiZmeHj48P06dPVcnfv3uX27dvZijkzsbGxFC1aFDs7OxRFydYvkszMzF452PbSpUucPXtW/RweHs5///1HmTJlqFWrFlevXtW6yJ8+fZrk5GR8fX3ZtWsX9+/fB+Dnn39+o+1q2bIl8+fPVwfMp6SkZJgUv+jF4yazWOvXr8+uXbvU8U5Lly7NtO6NGzeSmJhIWloay5cvp0GDBuq8wYMH07lzZypWrEjZsmUzXH7EiBEsW7aMnTt3qtNu377N4sWLMTc3p3Llyur+un79On///Te1a9cG4L333uPYsWMAbNmyhcTExNfui4z2R0b09fXp06cPLVu2xN/fH0tLyyzVLcSrSPIjCo1ly5ZRqVIlPvzwQypWrEjFihU5fPgwVlZWODg48OWXX1KtWjXq16+vdXINCgrC29ubypUrU7t2bb777jssLCz4+OOPSUxMpFKlSvTt2xcbGxtWrVpFp06dqFSpEgsWLHijX/WMHDmSypUr8+GHH+Ll5UWNGjVe2QJw7tw5atWqhZeXF1WrVqVLly54eXllWLZq1arqYNV69erRtm1bANasWcPFixfx9PTE09MTf39/NQnMCZ6enrRr146KFSvi6+tL6dKls7zs8OHD+eijjzIc8JyUlMTAgQPV7sQWLVowffp0KleuTPHixdm+fTvffPMNlSpVokKFCowcOZL09HQqVarEiBEjqFGjBj4+PpiZmWFhYZHt7erSpQudO3fG19eXSpUqUblyZfbv3//a5V48bjKL1cvLi9GjR1OrVi3q1KmDvb19pnXXrVuXVq1aUbFiRYoXL87AgQPVeW3btiUhISHTVjpPT092797NTz/9RJkyZfD09CQgIEBN4NesWcPq1aupVKkS/v7+/O9//8PJyQmAWbNm8cUXX1C7dm1OnTqVYQtrRnr37s3kyZPVAc+v0qtXL+7cuZNp/EJklUZRnhtCL4QokHx9ffnyyy9p3rx5XofyToiPj8fMzAx4+susa9euaY37KYiOHz9O586duXTpEnp6+e//3l9++YVFixbx119/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",
      "text/plain": [
       "<Figure size 600x400 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import matplotlib.pyplot as plt\n",
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "# Example of restructuring data for this purpose\n",
    "# This assumes cust contains columns for CustomerCountry, PlantKey, and CustomerKey (or equivalent customer identifier)\n",
    "data_aggregated = cust.groupby(['PlantKey', 'CustomerCountry']).agg({\n",
    "    'CustomerKey': 'count'  # Count of customers by PlantKey and CustomerCountry\n",
    "}).reset_index()\n",
    "\n",
    "# Sorting (optional, for better visualization)\n",
    "data_aggregated.sort_values(['PlantKey', 'CustomerKey'], inplace=True)\n",
    "\n",
    "# Unique countries for color mapping\n",
    "unique_countries = data_aggregated['CustomerCountry'].unique()\n",
    "colors = plt.cm.tab20(np.linspace(0, 1, len(unique_countries)))\n",
    "country_color_map = {country: color for country, color in zip(unique_countries, colors)}\n",
    "\n",
    "# Plotting\n",
    "plt.figure(figsize=(6, 4))\n",
    "\n",
    "previous_plant = None\n",
    "bottoms = np.zeros(len(data_aggregated['PlantKey'].unique()))\n",
    "\n",
    "for _, row in data_aggregated.iterrows():\n",
    "    plant_index = np.where(data_aggregated['PlantKey'].unique() == row['PlantKey'])[0][0]\n",
    "    plt.bar(row['PlantKey'], row['CustomerKey'], bottom=bottoms[plant_index], \n",
    "            color=country_color_map[row['CustomerCountry']], label=row['CustomerCountry'])\n",
    "    bottoms[plant_index] += row['CustomerKey']\n",
    "\n",
    "plt.title('Customers per Plant Segmented by Country', size = 8)\n",
    "plt.xlabel('PlantKey', size = 8)\n",
    "plt.ylabel('Number of Customers', size = 8)\n",
    "plt.xticks(rotation=45)\n",
    "plt.legend(title='Country', bbox_to_anchor=(0.5, -0.15), loc='upper center', ncol=4, fontsize='small', frameon=False)\n",
    "#plt.legend(title='Country', bbox_to_anchor=(1.05, 1), loc='upper left')\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 65,
   "id": "543f3410-17c0-41c4-83ab-26fc62db804a",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "  RequestedDeliveryMonth  MaterialKey  PlantKey  Quantity  MaterialPlantKey\n",
      "0             2022-01-01            1         4     15978             10004\n",
      "1             2022-01-01            1         5      5360             10005\n",
      "(480, 5)\n"
     ]
    }
   ],
   "source": [
    "frcst_file = os.path.join(data_directory, 'Forecast.csv')\n",
    "frcst = pd.read_csv(frcst_file)\n",
    "print(frcst.head(2))\n",
    "print(frcst.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 66,
   "id": "b8271a2c-7c43-4e20-8901-66e45b41c5a8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Inventory.csv:\n",
      "   MaterialKey  PlantKey  MaterialPlantKey SnapshotDate  \\\n",
      "0            1         4             10004   2021-12-31   \n",
      "1            1         5             10005   2021-12-31   \n",
      "\n",
      "   GrossInventoryQuantity  OnShelfInventoryQuantity  InTransitQuantity  \n",
      "0                  1753.0                      1626              127.0  \n",
      "1                   794.0                       746               48.0  \n",
      "(260, 7)\n"
     ]
    }
   ],
   "source": [
    "# Inventory.csv\n",
    "inventory_file = os.path.join(data_directory, 'Inventory.csv')\n",
    "inventory = pd.read_csv(inventory_file)\n",
    "print(\"Inventory.csv:\")\n",
    "print(inventory.head(2))\n",
    "print(inventory.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 67,
   "id": "6920016e-cffa-454f-9ec3-7b0d93bbe845",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "MaterialPlantRelation.csv:\n",
      "   MaterialKey  PlantKey  MaterialPlantKey  VendorKey  StandardCost Currency  \\\n",
      "0            1         4             10004       1001       2680.05      EUR   \n",
      "1            1         5             10005       1002      11547.17      PLN   \n",
      "\n",
      "   ProductionTime  InboundTransportationTime  GoodReceiptProcessingTime  \\\n",
      "0              20                          1                          2   \n",
      "1              20                          1                          2   \n",
      "\n",
      "   TotalInboundLeadTime  SafetyStockQty  \n",
      "0                    23          1000.0  \n",
      "1                    23           500.0  \n",
      "(109, 11)\n"
     ]
    }
   ],
   "source": [
    "# MaterialPlantRelation.csv\n",
    "material_plant_relation_file = os.path.join(data_directory, 'MaterialPlantRelation.csv')\n",
    "material_plant_relation = pd.read_csv(material_plant_relation_file)\n",
    "print(\"MaterialPlantRelation.csv:\")\n",
    "print(material_plant_relation.head(2))\n",
    "print(material_plant_relation.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 68,
   "id": "9b3af2e1-f5a0-4c0a-a6df-3ded04ccc00f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Materials.csv:\n",
      "   Material  MaterialKey      MaterialType MaterialDescription  \\\n",
      "0  EVCB-001            1  Finished Product      EV Car Battery   \n",
      "1    HB-001            2  Finished Product        Home Battery   \n",
      "\n",
      "       Product Category Component  \n",
      "0   EV Car Battery - FP       NaN  \n",
      "1  EV Home Battery - FP       NaN  \n",
      "(33, 6)\n"
     ]
    }
   ],
   "source": [
    "# Materials.csv\n",
    "materials_file = os.path.join(data_directory, 'Materials.csv')\n",
    "materials = pd.read_csv(materials_file)\n",
    "print(\"Materials.csv:\")\n",
    "print(materials.head(2))\n",
    "print(materials.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 73,
   "id": "36c3fe32-d4e4-43f0-8455-384a70a5ae54",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Plants.csv:\n",
      "   PlantKey Plant            PlantType           PlantName PlantCity  \\\n",
      "0         1  ANT1           Production  Antwerp Production   Antwerp   \n",
      "1         2  WRO1           Production  Wrocław Production   Wrocław   \n",
      "2         3  LYO1           Production     Lyon Production      Lyon   \n",
      "3         4  ANT2  Distribution Center          Antwerp DC   Antwerp   \n",
      "4         5  WRO2  Distribution Center          Wrocław DC   Wrocław   \n",
      "\n",
      "  PlantPostalCode         PlantStreet  \n",
      "0            2030         Scheldelaan  \n",
      "1          54-202            Legnicka  \n",
      "2           69160  Av. Mathieu Misery  \n",
      "3            2030         Scheldelaan  \n",
      "4          54-202            Legnicka  \n"
     ]
    }
   ],
   "source": [
    "# Plants.csv\n",
    "plants_file = os.path.join(data_directory, 'Plants.csv')\n",
    "plants = pd.read_csv(plants_file)\n",
    "print(\"Plants.csv:\")\n",
    "print(plants.head())\n",
    "#print(plants.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 70,
   "id": "b2694677-0aef-4b98-a45c-60128c0085ea",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Purchases.csv:\n",
      "   PurchaseOrder PurchaseOrderCreationDate  VendorKey  PlantKey  MaterialKey  \\\n",
      "0     4500000001                2023-06-07       1002         5            1   \n",
      "1     4500000002                2023-03-05       1001         7            1   \n",
      "\n",
      "   MaterialPlantKey  PurchaseOrderQuantity PlannedGoodsReceiptDate  \\\n",
      "0             10005                     69              2023-06-30   \n",
      "1             10007                     80              2023-03-28   \n",
      "\n",
      "  ActualGoodsReceiptDate PlannedArrivalDateYard ActualArrivalDateYard  \\\n",
      "0             2023-07-04             2023-06-28            2023-07-02   \n",
      "1             2023-03-24             2023-03-26            2023-03-26   \n",
      "\n",
      "  PlannedVendorShipmentDate ActualVendorShipmentDate  \n",
      "0                2023-06-27               2023-07-01  \n",
      "1                2023-03-25               2023-03-25  \n",
      "(20000, 13)\n"
     ]
    }
   ],
   "source": [
    "# Purchases.csv\n",
    "purchases_file = os.path.join(data_directory, 'Purchases.csv')\n",
    "purchases = pd.read_csv(purchases_file)\n",
    "print(\"Purchases.csv:\")\n",
    "print(purchases.head(2))\n",
    "print(purchases.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 71,
   "id": "0840445e-c0bc-475b-b877-753ed73168c8",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Sales.csv:\n",
      "   SalesOrder  SalesOrderItem SalesOrderCreationDate  CustomerKey  \\\n",
      "0    10000001              10             2024-10-08          349   \n",
      "1    10000002              10             2023-05-27          759   \n",
      "\n",
      "   MaterialKey  OrderQuantity  PlantKey  MaterialPlantKey SalesDocType  \\\n",
      "0            1             26         4             10004      Regular   \n",
      "1            1             20         5             10005      Regular   \n",
      "\n",
      "  RequestedDeliveryDate DeliveryDate  HighOrderQtyFlag  \n",
      "0            2024-11-15   2024-11-15                 0  \n",
      "1            2023-06-15   2023-06-12                 0  \n",
      "(100000, 12)\n"
     ]
    }
   ],
   "source": [
    "# Sales.csv\n",
    "sales_file = os.path.join(data_directory, 'Sales.csv')\n",
    "sales = pd.read_csv(sales_file)\n",
    "print(\"Sales.csv:\")\n",
    "print(sales.head(2))\n",
    "print(sales.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "id": "e15ec21f-da9d-483d-8297-e2101e096390",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Unnamed: 0_x</th>\n",
       "      <th>CustomerKey</th>\n",
       "      <th>CustomerName</th>\n",
       "      <th>CustomerCountry</th>\n",
       "      <th>CustomerCity</th>\n",
       "      <th>CustomerPostalCode</th>\n",
       "      <th>CustomerStreet</th>\n",
       "      <th>PlantKey_x</th>\n",
       "      <th>Unnamed: 0_y</th>\n",
       "      <th>SalesOrder</th>\n",
       "      <th>SalesOrderItem</th>\n",
       "      <th>SalesOrderCreationDate</th>\n",
       "      <th>MaterialKey</th>\n",
       "      <th>OrderQuantity</th>\n",
       "      <th>PlantKey_y</th>\n",
       "      <th>MaterialPlantKey</th>\n",
       "      <th>SalesDocType</th>\n",
       "      <th>RequestedDeliveryDate</th>\n",
       "      <th>DeliveryDate</th>\n",
       "      <th>HighOrderQtyFlag</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>O'Hara-MacGyver</td>\n",
       "      <td>Germany</td>\n",
       "      <td>Hamburg</td>\n",
       "      <td>22041</td>\n",
       "      <td>36 Westport Court</td>\n",
       "      <td>4</td>\n",
       "      <td>680</td>\n",
       "      <td>10000680</td>\n",
       "      <td>10</td>\n",
       "      <td>2024-07-21</td>\n",
       "      <td>2</td>\n",
       "      <td>18</td>\n",
       "      <td>4</td>\n",
       "      <td>20004</td>\n",
       "      <td>Regular</td>\n",
       "      <td>2024-08-26</td>\n",
       "      <td>2024-09-09</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>O'Hara-MacGyver</td>\n",
       "      <td>Germany</td>\n",
       "      <td>Hamburg</td>\n",
       "      <td>22041</td>\n",
       "      <td>36 Westport Court</td>\n",
       "      <td>4</td>\n",
       "      <td>731</td>\n",
       "      <td>10000731</td>\n",
       "      <td>10</td>\n",
       "      <td>2024-02-06</td>\n",
       "      <td>2</td>\n",
       "      <td>19</td>\n",
       "      <td>4</td>\n",
       "      <td>20004</td>\n",
       "      <td>Regular</td>\n",
       "      <td>2024-03-04</td>\n",
       "      <td>2024-02-28</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>O'Hara-MacGyver</td>\n",
       "      <td>Germany</td>\n",
       "      <td>Hamburg</td>\n",
       "      <td>22041</td>\n",
       "      <td>36 Westport Court</td>\n",
       "      <td>4</td>\n",
       "      <td>757</td>\n",
       "      <td>10000757</td>\n",
       "      <td>10</td>\n",
       "      <td>2022-06-01</td>\n",
       "      <td>1</td>\n",
       "      <td>16</td>\n",
       "      <td>4</td>\n",
       "      <td>10004</td>\n",
       "      <td>Regular</td>\n",
       "      <td>2022-07-01</td>\n",
       "      <td>2022-06-30</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>O'Hara-MacGyver</td>\n",
       "      <td>Germany</td>\n",
       "      <td>Hamburg</td>\n",
       "      <td>22041</td>\n",
       "      <td>36 Westport Court</td>\n",
       "      <td>4</td>\n",
       "      <td>3345</td>\n",
       "      <td>10003345</td>\n",
       "      <td>10</td>\n",
       "      <td>2022-11-13</td>\n",
       "      <td>1</td>\n",
       "      <td>19</td>\n",
       "      <td>4</td>\n",
       "      <td>10004</td>\n",
       "      <td>Regular</td>\n",
       "      <td>2022-12-29</td>\n",
       "      <td>2022-12-27</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>O'Hara-MacGyver</td>\n",
       "      <td>Germany</td>\n",
       "      <td>Hamburg</td>\n",
       "      <td>22041</td>\n",
       "      <td>36 Westport Court</td>\n",
       "      <td>4</td>\n",
       "      <td>3473</td>\n",
       "      <td>10003473</td>\n",
       "      <td>10</td>\n",
       "      <td>2022-05-11</td>\n",
       "      <td>2</td>\n",
       "      <td>20</td>\n",
       "      <td>4</td>\n",
       "      <td>20004</td>\n",
       "      <td>Regular</td>\n",
       "      <td>2022-05-30</td>\n",
       "      <td>2022-05-25</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Unnamed: 0_x  CustomerKey     CustomerName CustomerCountry CustomerCity  \\\n",
       "0             1            1  O'Hara-MacGyver         Germany      Hamburg   \n",
       "1             1            1  O'Hara-MacGyver         Germany      Hamburg   \n",
       "2             1            1  O'Hara-MacGyver         Germany      Hamburg   \n",
       "3             1            1  O'Hara-MacGyver         Germany      Hamburg   \n",
       "4             1            1  O'Hara-MacGyver         Germany      Hamburg   \n",
       "\n",
       "  CustomerPostalCode     CustomerStreet  PlantKey_x  Unnamed: 0_y  SalesOrder  \\\n",
       "0              22041  36 Westport Court           4           680    10000680   \n",
       "1              22041  36 Westport Court           4           731    10000731   \n",
       "2              22041  36 Westport Court           4           757    10000757   \n",
       "3              22041  36 Westport Court           4          3345    10003345   \n",
       "4              22041  36 Westport Court           4          3473    10003473   \n",
       "\n",
       "   SalesOrderItem SalesOrderCreationDate  MaterialKey  OrderQuantity  \\\n",
       "0              10             2024-07-21            2             18   \n",
       "1              10             2024-02-06            2             19   \n",
       "2              10             2022-06-01            1             16   \n",
       "3              10             2022-11-13            1             19   \n",
       "4              10             2022-05-11            2             20   \n",
       "\n",
       "   PlantKey_y  MaterialPlantKey SalesDocType RequestedDeliveryDate  \\\n",
       "0           4             20004      Regular            2024-08-26   \n",
       "1           4             20004      Regular            2024-03-04   \n",
       "2           4             10004      Regular            2022-07-01   \n",
       "3           4             10004      Regular            2022-12-29   \n",
       "4           4             20004      Regular            2022-05-30   \n",
       "\n",
       "  DeliveryDate  HighOrderQtyFlag  \n",
       "0   2024-09-09                 0  \n",
       "1   2024-02-28                 0  \n",
       "2   2022-06-30                 0  \n",
       "3   2022-12-27                 0  \n",
       "4   2022-05-25                 0  "
      ]
     },
     "execution_count": 59,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# sales year\n",
    "# Requested Delivery Date vs Delivery Date \n",
    "country_sales = pd.merge(cust, sales, on='CustomerKey')\n",
    "# Aggregate sales by country and find the most common PlantKey for each country\n",
    "# sales_and_plant_by_country = country_sales.groupby('CustomerCountry').agg({\n",
    "#     'OrderQuantity': 'sum',  # Sum of sales\n",
    "#     'PlantKey': lambda x: x.mode()[0]  # Most common PlantKey\n",
    "# }).reset_index()\n",
    "\n",
    "country_sales.head(5)\n",
    "#sales_and_plant_by_country\n",
    "# # Sorting by sales for better visualization\n",
    "# sales_and_plant_by_country.sort_values('OrderQuantity', inplace=True)\n",
    "\n",
    "# # Step 3: Prepare color mapping\n",
    "# unique_plants = sales_and_plant_by_country['PlantKey'].unique()\n",
    "# colors = plt.cm.tab20(np.linspace(0, 1, len(unique_plants)))\n",
    "# plant_color_map = {plant: color for plant, color in zip(unique_plants, colors)}\n",
    "\n",
    "# # Step 4: Plotting\n",
    "# plt.figure(figsize=(10, 4))\n",
    "# for _, row in sales_and_plant_by_country.iterrows():\n",
    "#     plt.bar(row['CustomerCountry'], row['OrderQuantity'], color=plant_color_map[row['PlantKey']])\n",
    "\n",
    "# plt.title('Sales per Country')\n",
    "# plt.ylabel('Order Quantity')\n",
    "# plt.xticks(rotation=45, size=8)\n",
    "\n",
    "# # Creating a legend\n",
    "# from matplotlib.patches import Patch\n",
    "# legend_elements = [Patch(facecolor=plant_color_map[plant], label=plant) for plant in unique_plants]\n",
    "# plt.legend(handles=legend_elements, title='PlantKey', bbox_to_anchor=(1.05, 1), loc='upper left')\n",
    "\n",
    "# plt.tight_layout()\n",
    "# plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 72,
   "id": "ff1df934-40ee-45da-8015-c0c7a4ad9753",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Vendors.csv:\n",
      "   VendorKey VendorTier          VendorName VendorCountry VendorCity  \\\n",
      "0       1001         T0  Antwerp Production       Belgium    Antwerp   \n",
      "1       1002         T0  Wrocław Production        Poland    Wrocław   \n",
      "\n",
      "  VendorPostalCode VendorStreet  \n",
      "0             2030  Scheldelaan  \n",
      "1           54-202     Legnicka  \n",
      "(9, 7)\n"
     ]
    }
   ],
   "source": [
    "# Vendors.csv\n",
    "vendors_file = os.path.join(data_directory, 'Vendors.csv')\n",
    "vendors = pd.read_csv(vendors_file)\n",
    "print(\"Vendors.csv:\")\n",
    "print(vendors.head(2))\n",
    "print(vendors.shape)"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
