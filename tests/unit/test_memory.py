from memory.short_term_memory import ShortTermMemory

def test_short_term_memory():
    mem = ShortTermMemory()
    mem.store_prompt("hello")
    mem.store_response("hi there")
    recalled = mem.recall()
    assert recalled["prompt"] == "hello"
    assert recalled["response"] == "hi there"
