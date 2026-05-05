class TokenBudget:
    def __init__(self, max_tokens: int):
        self.max_tokens = max_tokens
        self.used_tokens = 0

    def can_proceed(self, estimated_tokens: int) -> bool:
        return (self.used_tokens + estimated_tokens) <= self.max_tokens

    def record_usage(self, actual_tokens: int):
        self.used_tokens += actual_tokens

budget = TokenBudget(max_tokens=50000)  # per session

# while agent.has_next_step():
#     estimated = agent.estimate_next_step_tokens()
#     if not budget.can_proceed(estimated):
#         agent.respond("I have reached my processing limit for this session. "
#                       "Let me summarize what I have found so far.")
#         break
#     result = agent.execute_next_step()
#     budget.record_usage(result.tokens_used)