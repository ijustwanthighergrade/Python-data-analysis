# importexcel.py
import pandas as pd
import os
import django
from django.utils import timezone

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "analysis.settings")
django.setup()

from home.models import MarriageSurvey  
MarriageSurvey.objects.all().delete()

# Path to Excel file
excel_file_path = r"C:\Users\DAIYUNWU\Desktop\Python-data-analysis\analysis\home\data\collect.xlsx"

# Read the Excel file and insert data into the database
df = pd.read_excel(excel_file_path)

for _, row in df.iterrows():
    timestamp_str = str(row["時間戳記"])
    timestamp = timezone.make_aware(pd.Timestamp(timestamp_str).to_pydatetime())

    MarriageSurvey.objects.create(
        timestamp=timestamp,
        gender=row["生理性別"],
        education=row["最高學歷"],
        age=row["您的年齡"],
        salary=row["目前月薪資水平(台幣)"],
        is_married=row["您是否已婚？"],
        marriage_intention = row["您目前是否有結婚意願(不論單身與否)"],
        agree_buying_house = row["您認同買房是影響多數人結婚的重要因素嗎？"],
        buying_house_influence = row["請問買房影響您結婚意願的程度為？"],
        marriage_house_requirement = row["您對結婚一定得買房的認同度為何？"],
        afford_house_price = row["請問您認為自己目前薪資能獨自負擔逐年攀升的房價的程度為？"],
        buying_house_impact_life = row["您認同買房會影響到個人生活水平的程度為？"],
        government_support = row["您認為政府在買房上已擁有完善配套措施的程度為？"],
        family_planning = row["想要與心愛的人共組家庭"],
        desire_for_children = row["想要小孩"],
        legal_recognition = row["想要讓伴侶關係被法律所認同"],
        tradition = row["傳統上結婚是人生的必經之路"],
        responsibility_sharing = row["想要伴侶一同承擔責任"],
        sacrifice_lifestyle = row["不想因為結婚犧牲現有生活水平"],
        affordability = row["無法負擔高額房價"],
        marriage_expenses_affordability = row["無法負擔結婚開銷"],
        stable_career_before_family = row["想要先穩定事業再組建家庭"],
        child_rearing_cost_affordability = row["無法負擔子女教養費用"],
        non_economic_factor_relationship = row["只需要情感需求，不想綁定法律義務"],
        family_adjustment_concerns = row["害怕要與對方家庭磨合"],
        trustworthiness = row["不知是否對方值得信任"],
        fear_of_commitment = row["不想養小孩"],
        freedom_loss_after_marriage = row["婚後會失去自由"],
        no_partner = row["沒有對象"],
        fear_of_marriage_failure = row["害怕婚姻失敗"],
        anycommond = row["任何指教"]
        )