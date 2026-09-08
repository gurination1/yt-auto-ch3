import os
try:
    from dotenv import load_dotenv
    load_dotenv()
    for ep in [".env", "../.env", "../../.env", "/mnt/g/yt-auto-fleet/.env"]:
        if os.path.exists(ep):
            load_dotenv(ep, override=False)
except Exception:
    pass

# Auto-load local_env.sh if present to populate environment variables
def _autoload_local_env():
    for env_path in [".env", "local_env.sh", "../local_env.sh",  "/root/local_env.sh"]:
        if os.path.exists(env_path):
            try:
                with open(env_path, "r", encoding="utf-8") as f:
                    for line in f:
                        line = line.strip()
                        if not line or line.startswith("#"):
                            continue
                        if line.startswith("export "):
                            line = line[7:]
                        if "=" in line:
                            k, v = line.split("=", 1)
                            k = k.strip()
                            v = v.strip().strip('"').strip("'")
                            if k and k not in os.environ and v:
                                os.environ[k] = v
            except Exception:
                pass

_autoload_local_env()

# ── Gemini Key Pool ──────────────────────────────────────────────────────────
def _load_keys() -> list[str]:
    keys: list[str] = []
    multi = os.environ.get("GEMINI_API_KEYS", "").strip()
    if multi:
        keys.extend(k.strip() for k in multi.split(",") if k.strip())
    single = os.environ.get("GEMINI_API_KEY", "").strip()
    if single and not keys:
        keys.append(single)
    return list(dict.fromkeys(keys))

GEMINI_API_KEYS: list[str] = _load_keys()
GEMINI_API_KEY: str = GEMINI_API_KEYS[0] if GEMINI_API_KEYS else ""

GEMINI_JUDGE_API_KEY: str = os.environ.get("GEMINI_JUDGE_API_KEY", "").strip() or GEMINI_API_KEY

# ── Other APIs ───────────────────────────────────────────────────────────────
PEXELS_API_KEY   = os.environ.get("PEXELS_API_KEY", "")
PIXABAY_API_KEY  = os.environ.get("PIXABAY_API_KEY", "")
COVERR_API_KEY   = os.environ.get("COVERR_API_KEY", "")
NASA_API_KEY     = os.environ.get("NASA_API_KEY", "DEMO_KEY")
KLIPY_API_KEY    = os.environ.get("KLIPY_API_KEY", "")
FREESOUND_API_KEY = os.environ.get("FREESOUND_API_KEY", "")

# ── YouTube OAuth ────────────────────────────────────────────────────────────
YT_CLIENT_ID     = os.environ.get("YT_CLIENT_ID", "")
YT_CLIENT_SECRET = os.environ.get("YT_CLIENT_SECRET", "")
YT_REFRESH_TOKEN = os.environ.get("YT_REFRESH_TOKEN", "")

# ── Gemini Models ────────────────────────────────────────────────────────────
GEMINI_FLASH        = "gemini-2.5-flash"
GEMINI_FLASH_BACKUP = "gemini-2.5-flash-lite"
GEMINI_PRO          = "gemini-2.5-flash"
GEMINI_TTS_MODEL    = "gemini-2.5-flash-preview-tts"
GEMINI_API_BASE     = "https://generativelanguage.googleapis.com/v1beta"

GEMINI_VOICES    = ["Fenrir", "Puck", "Charon", "Orus", "Kore"]
KOKORO_VOICES    = ["af_heart","af_bella","af_nicole","af_sarah","af_sky","af_aoede","am_adam","am_michael","am_fenrir","am_puck"]

# ── Video Specs ──────────────────────────────────────────────────────────────
SHORTS_W, SHORTS_H = 1080, 1920
LONG_W,   LONG_H   = 1920, 1080
FPS                 = 30
TOPIC_LOG_SIZE      = 90

HOOK_PATTERNS = [
    "The {topic} fact that breaks a rule you learned in school",
    "In exactly 30 seconds you'll never see {topic} the same way",
    "Scientists found something inside {topic} that shouldn't exist",
    "The {topic} detail that 99% of people never notice — even experts",
    "What {topic} does when no one is watching will disturb you",
    "The one thing about {topic} that every textbook gets wrong",
    "This single {topic} fact overturns 100 years of assumptions",
    "You've seen {topic} your whole life. You've never actually seen it.",
]

THUMBNAIL_LAYOUTS = [
    "dark_top_bar",
    "centered_gradient",
    "bottom_third",
    "split_left",
]

# ── Channel Boundary & Topic Isolation (Channel 3: History & Warfare Tactics) ──
CHANNEL_NICHE = os.environ.get("CHANNEL_NICHE", "history")

CHANNEL_BOUNDARY = {
    "channel_id": "ch3",
    "name": "Channel 3: History & Warfare Tactics",
    "niche_description": "Ancient siege weapons, mechanical warfare engineering, Roman military doctrines, battlefield tactics and unit formations, catastrophic empire collapses, and declassified ancient wartime strategies.",
    "allowed_subclusters": [
        "ancient siege weapons, torsion catapults, and mechanical warfare",
        "roman military tactics, legion formations, and battlefield discipline",
        "ancient battle engineering, trench fortifications, and naval siphons",
        "catastrophic empire collapses, tactical blunders, and decisive ambushes",
        "declassified ancient warfare strategies, historical espionage, and secret fortresses"
    ],
    "strict_negative_constraints": [
        "NO space science, astronomy, cosmos, stars, astrophysics, NASA, galaxies, or dark energy.",
        "NO animals, wildlife, zoology, marine biology, or species evolutionary trivia.",
        "NO modern civil tunneling, modern skyscrapers, modern megaprojects, or modern transport systems.",
        "NO modern crypto, stocks, modern finance, fintech, or corporate startups."
    ],
    "negative_keywords": [
        "astronomy",
        "astrophysics",
        "cosmos",
        "galaxy",
        "telescope",
        "nasa",
        "dark energy",
        "quantum mechanics",
        "nanotechnology",
        "superconductor",
        "subatomic",
        "particle collider",
        "wildlife documentary",
        "zoology",
        "marine biology",
        "insect species",
        "predator animal",
        "venomous snake",
        "jellyfish sting",
        "amphibian",
        "parasite fungi",
        "tunnel boring machine",
        "tbm",
        "modern skyscraper",
        "subsea tunnel",
        "modern dam",
        "suspension bridge",
        "highway expansion",
        "excavator bagger",
        "crypto",
        "bitcoin",
        "blockchain",
        "stock market",
        "hedge fund",
        "venture capital",
        "fintech"
    ]
}

CHANNEL_SUBCLUSTERS = CHANNEL_BOUNDARY["allowed_subclusters"]
SCIENCE_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
NATURE_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
NATURAL_WORLD_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
HISTORY_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
MYSTERY_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
ENGINEERING_SUBCLUSTERS = CHANNEL_SUBCLUSTERS
NICHE_SUBCLUSTERS = CHANNEL_SUBCLUSTERS

YT_CATEGORY_EDUCATION = "27"
YT_CATEGORY_SCIENCE   = "27"
YT_CATEGORY_DEFAULT   = "27"
NASA_BROLL_ENABLED    = False

RICH_FALLBACK_TOPICS = [
    {
        "topic": "The Claw of Archimedes: The ancient mechanical crane that hooked and capsized Roman warships at Syracuse",
        "short_hook": "Archimedes built a giant mechanical claw to sink ships.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient siege weapons, torsion catapults, and mechanical warfare"
    },
    {
        "topic": "The Roman Corvus: The spiked assault boarding bridge that converted Mediterranean sea battles into land combat",
        "short_hook": "How Rome's spiked bridge broke Carthage's navy.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "roman military tactics, legion formations, and battlefield discipline"
    },
    {
        "topic": "The Siege of Tyre: How Alexander the Great built a kilometer-long ocean causeway to shatter an island fortress",
        "short_hook": "Alexander built a land bridge across the sea.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient battle engineering, trench fortifications, and naval siphons"
    },
    {
        "topic": "Byzantine Greek Fire: The pressurized chemical naval flamethrower that continued burning on ocean water",
        "short_hook": "The lost liquid fire that burned on top of water.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient battle engineering, trench fortifications, and naval siphons"
    },
    {
        "topic": "The Roman Testudo Formation: How interlocking scutum shields deflected arrows, heavy stones, and javelins",
        "short_hook": "The Roman shield turtle that deflected falling rocks.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "roman military tactics, legion formations, and battlefield discipline"
    },
    {
        "topic": "The Battle of Cannae: How Hannibal's double envelopment crescent tactic surrounded 70,000 Roman legionaries",
        "short_hook": "Hannibal's tactical trap annihilated 70,000 Romans in hours.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "catastrophic empire collapses, tactical blunders, and decisive ambushes"
    },
    {
        "topic": "The Counterweight Trebuchet: The medieval mechanical siege engine hurling 300-pound boulders over 300 yards",
        "short_hook": "The medieval super-weapon that shattered fortress walls.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient siege weapons, torsion catapults, and mechanical warfare"
    },
    {
        "topic": "The Siege of Alesia: How Julius Caesar constructed two concentric 15-mile fortified walls while besieged himself",
        "short_hook": "Caesar built a wall to surround an army while surrounded.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient battle engineering, trench fortifications, and naval siphons"
    },
    {
        "topic": "The Roman Ballista: The torsion-powered bolt thrower that pinned armored cavalry through solid wood shields",
        "short_hook": "The Roman sniper weapon that pierced solid shields.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient siege weapons, torsion catapults, and mechanical warfare"
    },
    {
        "topic": "The Mongol Feigned Retreat: The psychological cavalry doctrine that lured disciplined armies into annihilating traps",
        "short_hook": "The fake retreat tactic that conquered the world.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "catastrophic empire collapses, tactical blunders, and decisive ambushes"
    },
    {
        "topic": "Great Wall Sticky Rice Mortar: The ancient chemical recipe of amylopectin that made military fortresses earthquake-proof",
        "short_hook": "The Great Wall was held together by sticky rice!",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient battle engineering, trench fortifications, and naval siphons"
    },
    {
        "topic": "The Spartan Hoplite Phalanx: How bronze aspis shields and 9-foot dory spears built an impenetrable human wall",
        "short_hook": "The Spartan shield wall that crushed opposing armies.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "roman military tactics, legion formations, and battlefield discipline"
    },
    {
        "topic": "The Battle of Carrhae: How Parthian horse archers used camel supply trains to continuously bombard Crassus",
        "short_hook": "How horse archers wiped out Rome's richest man.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "catastrophic empire collapses, tactical blunders, and decisive ambushes"
    },
    {
        "topic": "The Roman Onager: The single-arm torsion siege engine named after the wild donkey for its violent recoil",
        "short_hook": "The Roman siege engine with the kick of a wild donkey.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient siege weapons, torsion catapults, and mechanical warfare"
    },
    {
        "topic": "The Fall of Constantinople (1453): How the Orban super-bombard shattered the 1,000-year-old Theodosian stone walls",
        "short_hook": "The colossal super-cannon that ended the Byzantine Empire.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "catastrophic empire collapses, tactical blunders, and decisive ambushes"
    },
    {
        "topic": "The Hussite War Wagons: The mobile medieval fortified rolling fortresses that neutralized heavy knight charges",
        "short_hook": "The peasants who built rolling tanks out of farm wagons.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient siege weapons, torsion catapults, and mechanical warfare"
    },
    {
        "topic": "Roman Military Decimation: The brutal disciplinary punishment where disgraced cohorts bludgeoned every tenth man",
        "short_hook": "Rome's most brutal military punishment: Decimation.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "roman military tactics, legion formations, and battlefield discipline"
    },
    {
        "topic": "Cataphract Shock Cavalry: The fully armored horse-and-rider juggernauts that trampled Mediterranean battle lines",
        "short_hook": "The ancient ironclad cavalry that crushed foot soldiers.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient siege weapons, torsion catapults, and mechanical warfare"
    },
    {
        "topic": "The Battle of Teutoburg Forest: How Arminius trapped three Roman legions in marshy bottlenecks to wipe out 20,000 men",
        "short_hook": "Three entire Roman legions vanished in this German forest.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "catastrophic empire collapses, tactical blunders, and decisive ambushes"
    },
    {
        "topic": "The Siege of Masada: How Roman soldiers constructed a colossal 375-foot earthen assault ramp up a sheer mesa",
        "short_hook": "Romans built a 375-foot dirt mountain to breach a fortress.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient battle engineering, trench fortifications, and naval siphons"
    },
    {
        "topic": "Persian Scythed Chariots: The spinning iron wheel-blade combat chariots engineered to sever enemy infantry ranks",
        "short_hook": "The ancient battle chariots with spinning wheel blades.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "ancient siege weapons, torsion catapults, and mechanical warfare"
    },
    {
        "topic": "The Roman Pilum Javelin: The soft iron neck designed to bend upon impact so enemies could not throw it back",
        "short_hook": "Why Roman javelins were engineered to bend on impact.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "roman military tactics, legion formations, and battlefield discipline"
    },
    {
        "topic": "The Battle of Agincourt: How English longbow stakes planted in muddy terrain halted French armored knights",
        "short_hook": "How wooden stakes and mud defeated France's greatest knights.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "catastrophic empire collapses, tactical blunders, and decisive ambushes"
    },
    {
        "topic": "The Anglo-Saxon Shield Wall: How interlocking Linden wood shields withstood cavalry impact at the Battle of Hastings",
        "short_hook": "The interlocking wooden wall that stopped heavy cavalry.",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "roman military tactics, legion formations, and battlefield discipline"
    },
    {
        "topic": "The Bronze Age Collapse: How the mysterious Sea Peoples demolished Mediterranean empires in less than 50 years",
        "short_hook": "Who were the mysterious Sea Peoples that destroyed empires?",
        "hook_type": "curiosity_gap",
        "for_format": "both",
        "subcluster": "catastrophic empire collapses, tactical blunders, and decisive ambushes"
    }
]

def validate_config():
    missing = []
    if not GEMINI_API_KEYS:
        missing.append("GEMINI_API_KEY or GEMINI_API_KEYS")
    
    check_vars = []
    if PEXELS_API_KEY:
        check_vars.append(("PEXELS_API_KEY", PEXELS_API_KEY))
    if os.environ.get("DISABLE_YT_UPLOAD") != "1":
        check_vars.extend([
            ("YT_CLIENT_ID", YT_CLIENT_ID),
            ("YT_CLIENT_SECRET", YT_CLIENT_SECRET),
            ("YT_REFRESH_TOKEN", YT_REFRESH_TOKEN)
        ])
    for var, val in check_vars:
        if not val:
            missing.append(var)
    if missing:
        raise ValueError(f"Missing required env vars: {', '.join(missing)}")
    n = len(GEMINI_API_KEYS)
    print(f"[Config] {n} Gemini generation key(s) loaded.")
    if GEMINI_JUDGE_API_KEY != GEMINI_API_KEY:
        print("[Config] Separate GEMINI_JUDGE_API_KEY active — Judge uses its own quota.")
    if COVERR_API_KEY:
        print("[Config] Coverr API: enabled (cinematic B-roll tier active).")
    if NASA_API_KEY:
        print(f"[Config] NASA API: enabled (key={'DEMO_KEY (rate-limited)' if NASA_API_KEY == 'DEMO_KEY' else 'custom'}).")
    if KLIPY_API_KEY:
        print("[Config] Klipy API: enabled (GIF/meme B-roll tier active).")
    if FREESOUND_API_KEY:
        print("[Config] Freesound API: enabled (CC0 ambient music tier active).")

# ── Social / Beacons Link ───────────────────────────────────────────────────
BEACONS_LINK = os.environ.get("BEACONS_LINK", "https://beacons.ai/edu_fun")

DEFAULT_GEMINI_VOICE = "Fenrir"
DEFAULT_KOKORO_VOICE = "am_adam"
VOICE_PITCH = 0.0
VOICE_RATE = 1.02
