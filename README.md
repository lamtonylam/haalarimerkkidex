# tsoha2024

- Overall patch dex, like PokeDex, but for collecting overall patches.
- Users can log in and register.
- Users can add patches to their collection. Data type include: name of patch, origin of patch (event or bought), maker of the patch ( for example a student guild), has it been sewed on yet
- Users can make their patch collection public, and other users can peek at other's collections.
- Users can remove their patch from the collection

### State of the app on second deadline 7.4.2024
- ✅ User login, logout and registration.
- ✅ Patch creation to general collection with: patch name, image
- ✅ Displaying general collection and specific patches
- ✅ Removing a patch from general collection
- ✅ Adding patches from the general collection to users' collection.
- ✅ Profile page that shows how many patches a user has added to their collection


# Using app on the web
**Note!** Please allow up to 10 seconds for the fly.io instance to wake up from sleep!  
https://haalarimerkkidex.fly.dev/

# Running locally
Prerequisites:
- python3 installed
- Pip (Python package manager)
- postgresql installed and server is running  https://github.com/hy-tsoha/local-pg


Clone the repository  
`git@github.com:lamtonylam/haalarimerkkidex.git`

Navigate into the correct folder containing the repository  
`cd haalarimerkkidex`

Create a .env environment file with the following variables.    
`DATABASE_URL=<local-postgres-address>`  
`SECRET_KEY=<your-secret-key>`  
`FLY_DEPLOYMENT=False`

Enable virtual environment  
`python3 -m venv venv`  
`source venv/bin/activate`

Install Flask  
`pip install flask`

Install dependencies  
`pip install -r requirements.txt`

Create database tables  
`psql < schema.sql`  
Then exit PSQL

Run Flask app  
`flask run`  
For continuous app builds run this command instead  
`flask run --debug`
