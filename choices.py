# Created by Stephanie Hernandez on 06/23/21

# Description: I created a dictionary based on the EmergencyAPI information with 
# the keys being countries and the value being their codes, so I can successufuly request 
# and get a specified country's emergency numbers. I also created an array with all the 
# names of the countries, so I could import it to the countyNums.py file to make the
# selections and make the code more readable.

codes = {
    'Afghanistan': 'AF',
    'Albania': 'AL',
    'Algeria': 'DZ',
    "Argentina": 'AR',
    "Armenia": 'AM',
    "Austria": 'AT',
    "Australia": 'AU',
    "Bahrain": 'BH',
    "Bangladesh": 'BD',
    "Barbados": 'BB',
    "Belarus": 'BY',
    "Belgium": 'BE',
    "Bolivia": 'BO',
    "Bosnia and Herzegovina": 'BA',
    "Botswana": 'BW',
    "Brazil": 'BR',
    "Brunei": 'BN', 
    "Bulgaria": 'BG',
    "Canada": 'CA',
    "Cayman Islands": 'KY',
    "Chad": 'TD',
    "Chile": 'CL',
    "China": 'CN',
    "Colombia": 'CL',
    "Costa Rica": 'CR',
    "Croatia": 'HR',
    "Cyprus": 'CY',
    "Czech Republic": 'CZ',
    "Denmark": 'DK',
    "Djibouti": 'DJ',
    "Dominican Republic": 'DO',
    "Ecuador": 'EC',
    "Egypt": 'EG',
    "Estonia": 'EE',
    "Faroe Islands": "FO",
    "Fiji": 'FJ',
    "Finland": 'FI',
    "France": 'FR',
    "Georgia": 'GE',
    "Germany": 'DE',
    "Ghana": 'GH',
    "Gibraltar": 'GI',
    "Greece": 'GR',
    "Greenland": 'Gl',
    "Guatemala": 'GT',
    "Guyana": 'GY',
    "Haiti": 'HT',
    "Honduras": 'HN',
    "Hong Kong": 'HK',
    "Hungary": 'HU',
    "Iceland": 'IS',
    "India": 'IN',
    "Indonesia": 'ID',
    "Iran": 'IR',
    "Iraq": 'IQ',
    "Ireland": 'IE',
    "Israel": 'IL',
    "Italy": 'IT',
    "Jamaica": 'JM',
    "Japan": 'JP',
    "Jordan": 'JO',
    "Kazakhstan": 'KZ',
    "Kuwait": 'KW',
    "Latvia": 'LV',
    "Lebanon": 'LB',
    "Lithuania": 'LT',
    "Luxembourg": 'LU',
    "Macau": 'MO',
    "Macedonia": 'MK',
    "Malaysia": 'MY',
    "Maldives": 'MV',
    "Mali": 'ML',
    "Malta": 'MT',
    "Mauritius": 'MU',
    "Mexico": 'MX',
    "Moldova": 'MD',
    "Monaco": 'MC',
    "Mongolia": 'MN',
    "Montenegro": 'ME',
    "Morocco": 'MA',
    "Myanmar": 'MM',
    "Nepal": 'NP',
    "Netherlands": 'NL',
    "New Zeland": 'NZ',
    "Nicaragua": 'NI',
    "Nigeria": 'NG',
    "North Korea": 'KP',
    "Northern Cyprus": 'CY',
    "Norway": 'NO',
    "Oman": 'OM',
    "Pakistan": 'PK',
    "Panama": 'PA',
    "Paraguay": 'PY',
    "Peru": 'PE',
    "Philippines": 'PH',
    "Poland": 'PL',
    "Portugal": 'PT',
    "Qatar": 'QA',
    "Romania": 'RO',
    "Russia": 'RU',
    "Rwanda": 'RW',
    "San Marino": 'SM',
    "Saudi Arabia": 'SA',
    "Serbia": 'RS',
    "Sierra Leone": 'SL',
    "Singapore": 'SG',
    "Slovakia": 'SK',
    "Slovenia": 'SI',
    "Solomon Islands": 'SB',
    "South Africa": 'ZA',
    "South Korea": 'KR',
    "Spain": 'ES',
    "Sri Lanka": 'LK',
    "Sudan": 'SD',
    "Suriname": 'SR',
    "Sweden": 'SE',
    "Switzerland": 'CH',
    "Syria": 'SY',
    "Taiwan": 'TW',
    "Tajikistan": 'TJ',
    "Thailand": 'TH',
    "Trinidad and Tobago": 'TT',
    "Tunisia": 'TN',
    "Turkey": 'TR',
    "Uganda": 'UG',
    "Ukraine": 'UA',
    "United Arab Emirates": 'AE',
    "United Kingdom": 'GB',
    "United States": 'US',
    "Uruguay": 'UY',
    "Vanuatu": 'VU',
    "Vatican City": 'VA',
    "Venezuela": 'VE',
    "Vietnam": 'VN',
    "Zambia": 'ZM',
    "Zimbabwe": 'ZW'
}

choices = [
    "Afghanistan", "Albania", "Algeria", "Argentina",
    "Armenia", "Austria", "Australia", "Bahrain",
    "Bangladesh", "Barbados", "Belarus", "Belgium",
    "Bolivia", "Bosnia and Herzegovina", "Botswana",
    "Brazil", "Brunei", "Bulgaria", "Canada",
    "Cayman Islands", "Chad", "Chile", "China",
    "Colombia", "Costa Rica", "Croatia", "Cyprus",
    "Czech Republic", "Denmark", "Djibouti", "Dominican Republic",
    "Ecuador", "Egypt", "Estonia", "Faroe Islands", "Fiji",
    "Finland", "France", "Georgia", "Germany", "Ghana",
    "Gibraltar", "Greece", "Greenland", "Guatemala",
    "Guyana", "Haiti", "Honduras", "Hong Kong", "Hungary",
    "Iceland", "India", "Indonesia", "Iran", "Iraq", "Ireland",
    "Israel", "Italy", "Jamaica", "Japan", "Jordan", "Kazakhstan",
    "Kuwait", "Latvia", "Lebanon", "Lithuania", "Luxembourg",
    "Macau", "Macedonia", "Malaysia", "Maldives", "Mali",
    "Malta", "Mauritius", "Mexico", "Moldova", "Monaco",
    "Mongolia", "Montenegro", "Morocco", "Myanmar", "Nepal",
    "Netherlands", "New Zeland", "Nicaragua", "Nigeria",
    "North Korea", "Northern Cyprus", "Norway", "Oman",
    "Pakistan", "Panama", "Paraguay", "Peru", "Philippines",
    "Poland", "Portugal", "Qatar", "Romania", "Russia",
    "Rwanda", "San Marino", "Saudi Arabia", "Serbia",
    "Sierra Leone", "Singapore", "Slovakia", "Slovenia",
    "Solomon Islands", "South Africa", "South Korea",
    "Spain", "Sri Lanka", "Sudan", "Suriname", "Sweden",
    "Switzerland", "Syria", "Taiwan", "Tajikistan",
    "Thailand", "Trinidad and Tobago", "Tunisia", "Turkey",
    "Uganda", "Ukraine", "United Arab Emirates", "United States",
    "Uruguay", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
    "Zambia", "Zimbabwe"
]