import os
from dotenv import load_dotenv
load_dotenv()
from langchain.chat_models import init_chat_model

os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API")

model = init_chat_model("groq:qwen/qwen3-32b")


prompt = """You are an elite running coach, biomechanics expert, and performance analyst.

Analyze my running data and provide:
- current fitness assessment
- estimated VO2 max
- endurance and speed analysis
- cadence and stride analysis
- whether I likely overstride
- ideal cadence range
- pace recommendations
- biggest weaknesses limiting performance
- realistic current 5K prediction
- best possible 5K after 1 month of optimized training
- weekly training recommendations
- recovery recommendations
- detailed 4-week improvement plan

Use quantitative reasoning, compare my metrics to runners at my level, and avoid generic advice. Explain WHY each recommendation matters. Be realistic but constructive.

I will provide:
- body weight
- age
- height
- running frequency
- gym/sports background
- sleep quality
- fatigue levels
- multiple runs with:
  - distance
  - pace
  - moving time
  - elevation
  - cadence (if available)
  - heart rate (if available)
  - perceived hardness

Output format:
1. Current fitness profile
2. Estimated VO2 max
3. Cadence + stride analysis
4. Pace zones:
   - easy
   - long run
   - tempo
   - threshold
   - interval
   - race pace
5. Biggest bottlenecks
6. Current estimated 5K
7. Best possible 5K after 1 month
8. Weekly training recommendations
9. 4-week improvement plan
10. Fastest realistic gains possible in 30 days"""