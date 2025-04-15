from Task import Task

def test_mark_done():
    task.mark_done()
    assert task.status == "done"