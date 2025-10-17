import contextvars
# Holds current test_id per test/thread
current_test_id = contextvars.ContextVar("current_test_id", default=None)