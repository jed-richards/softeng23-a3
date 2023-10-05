import pytest
from pathlib import Path
import os

from pmgr.project import Project, TaskException

@pytest.fixture(scope="function")
def testproj():
    tproj = Project('mytestproj')
    yield tproj
    tproj.delete()

def test_add(testproj):
    testproj.add_task('dosomething')
    assert 'dosomething' in testproj.get_tasks()

def test_add_already_in_tasks(testproj):
    testproj.add_task('dosomething')
    with pytest.raises(TaskException):
        testproj.add_task('dosomething')

def test_delete():
    tproj = Project("mytestproj")
    tproj.delete()
    assert tproj.filepath.exists() == False

def test_remove(testproj):
    testproj.add_task('dosomething')
    testproj.remove_task('dosomething')
    assert 'dosomething' not in testproj.get_tasks()

def test_remove_not_int_tasks(testproj):
    with pytest.raises(TaskException):
        testproj.remove_task('dosomething')

def test_remove_write(testproj):
    testproj.add_task('task1')
    testproj.add_task('task2')
    testproj.remove_task('task1')
    assert ['task2'] == testproj.get_tasks()

def test_get_tasks(testproj):
    testproj.add_task('task1')
    testproj.add_task('task2')
    testproj.add_task('task3')
    assert ['task1', 'task2', 'task3'] == testproj.get_tasks()

def test_get_tasks_empty(testproj):
    assert [] == testproj.get_tasks()
