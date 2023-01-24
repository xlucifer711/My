from os import getenv
from dotenv import load_dotenv

admins = {}
load_dotenv()

# client vars
API_ID = int(getenv("API_ID", "7452578"))
API_HASH = getenv("API_HASH", "061d67ee8eed9368c5cadabb4aa21efc")
BOT_TOKEN = getenv("BOT_TOKEN", "5471797925:AAHAUwrqZjohspI0_l15NL-5Gh5vhnYShr0")
SESSION_NAME = getenv("SESSION_NAME", "BABc3kyMbuhO99RG1nalxlBT0wwss0crY434W6WL3Ovz6qS7Rs6oBw6jD1l2dDyo5PHQJFGLXr-51LyHa_K0xfGjvE00ZZpr0yaXZQuKis-8oXhGP8CPFWHN5aMsnsRCf1MOuHnZ8F__Pg2tA2R_IY0HUHlDKh3g4Ui5JxbC4D2bH1tKmd1nPsr6smtlgudVbFLASGIVEgem6M2nMxfhThfNeTAellk7fvjpB91tfjZECTyUDeVc6apVyFR2NaCunk68KZPMUrlsjYPgfTkd8-rs77PNpsu_yZASQQPsNlcukGhDUGSyaLnWQsFVrIzQ_pmNom9exw9IjPJyBrIatW_CUMxiNwA")

# mandatory vars
OWNER_USERNAME = getenv("OWNER_USERNAME", "iiqllll ")
ALIVE_NAME = getenv("ALIVE_NAME", "pokemon")
BOT_USERNAME = getenv("BOT_USERNAME", "z_09bot")
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/X02lx/RrRRR")
UPSTREAM_BRANCH = getenv("UPSTREM_BRANCH", "main")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "GRO_UP_1")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL","S_EG_P") 

# database, decorators, handlers mandatory vars
MONGODB_URL = getenv("MONGODB_URL", "mongodb+srv://veez:mega@cluster0.heqnd.mongodb.net/veez?retryWrites=true&w=majority")
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! . $").split())
OWNER_ID = list(map(int, getenv("OWNER_ID", "5190136458").split()))
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5190136458").split()))

# image resources vars
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.png")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.png")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/d70bb6fa92728763c671f.png")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/430dcf25456f2bb38109f.png")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/cd5c96a3c7e8ae1913ef3.png")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/c83b000f004f01897fe18.png")
