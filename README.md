# CA1 - Nearby cafe + update own location to show on map

"Create and deploy a location-based services (LBS) application"


Database: PostgreSQL with PostGIS

Database management: PgAdmin4

Middle tier(s): Django

Front-end: Bootstrap v5

Mapping: Leaflet JS with OpenStreetMap

Deployment (middle tier(s) & database): Tried to deploy


- Challenges such as: Registered domain but could not get it successfully working.  Had issue with trying to do -a cloud-facing virtual machine with Docker installed. Used a certificate for only testing, could not get certbot working for deployment

- Learning outcome: Learned how to connect docker with postgis, pgadmin and django. Data gets inserted into the database correctly and applying CRUD operations. Successfully got Leaflet JS with OpenStreetMap to work based on user location.


Run docker-compose up --build and everything sets up

<img width="1512" alt="Screenshot 2024-11-10 at 20 51 35" src="https://github.com/user-attachments/assets/03724d4f-81f8-4027-884e-74b403008f55">
<img width="1512" alt="Screenshot 2024-11-10 at 20 51 46" src="https://github.com/user-attachments/assets/e1d4d410-b6a8-487a-8ee3-961fcccd0f4a">
<img width="1512" alt="Screenshot 2024-11-10 at 20 51 51" src="https://github.com/user-attachments/assets/f98e4684-f535-44cf-9ed2-c70b47c63f7f">
<img width="1512" alt="Screenshot 2024-11-10 at 20 51 54" src="https://github.com/user-attachments/assets/bc046014-9e6e-4190-bbb6-3b83a55d5041">
<img width="1512" alt="Screenshot 2024-11-10 at 20 52 01" src="https://github.com/user-attachments/assets/53910f1d-3b43-4963-ad73-b0d291ef1b00">
<img width="1512" alt="Screenshot 2024-11-10 at 20 52 13" src="https://github.com/user-attachments/assets/e00ee434-f45c-42b4-827d-594c08a5d636">
<img width="1512" alt="Screenshot 2024-11-10 at 20 52 33" src="https://github.com/user-attachments/assets/22a5fd29-38e0-40d8-8685-b2c248707be7">

