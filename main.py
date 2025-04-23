from agents.planner import planner_agent
from agents.developer import developer_agent
from agents.critic import critic_agent
from memory.faiss_store import init_memory

def run_workflow(user_task):
    print("🧠 PLANNER AGENT:")
    plan = planner_agent(user_task)
    print(plan)

    print("\n💻 DEVELOPER AGENT:")
    code = developer_agent(plan)
    print(code)

    print("\n🧐 CRITIC AGENT:")
    review = critic_agent(code)
    print(review)

    if "improve" in review.lower():
        print("\n🔁 DEVELOPER RETRY (Reflexive Loop):")
        improved_code = developer_agent(review)
        print(improved_code)

if __name__ == "__main__":
    memory = init_memory()
    run_workflow("Write a function to calculate compound interest")