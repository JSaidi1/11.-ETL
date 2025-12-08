import os
from pathlib import Path
from dotenv import load_dotenv


# ============================= Path to .env =============================
env_file = Path(__file__).parent.parent / "config" / "env" / "test.env"
load_dotenv(dotenv_path=env_file)

# ================= Warn if the env file does not exist ==================
if not Path(env_file).exists():
    print(f"\n[WARNING]: ENV_FILE not found: {env_file}\n")

# ========================================================================
#                            ENVs properties
# ========================================================================
class BaseSettings:
    """Base configuration shared across all environments"""
    # ----- Environment:
    CURRENT_ENV: str = os.getenv("APP_ENV", "TEST")  # Based on env_file

class TestSettings(BaseSettings):
    """Test configuration"""
    PATH_CSV_VENTES: str = "../data/raw/ventes.csv"
    PATH_CSV_VENTES_OUTPUT: str = "../data/output/rapport_ventes.xlsx"
    pass

class ProdSettings(BaseSettings):
    """Prod configuration"""
    pass

# --- Instantiate the correct settings based on ENV_FILE ---
if "prod.env" in str(env_file).lower():
    settings = ProdSettings()

if "test.env" in str(env_file).lower():
    settings = TestSettings()



# == Test in this file:
if __name__ == "__main__":
    print('\n==> in settings.py')
    print(settings.CURRENT_ENV)
    print(settings.PATH_CSV_VENTES)