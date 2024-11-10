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
