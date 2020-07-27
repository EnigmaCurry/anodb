import pytest
import anodb
import re

def test_anodb():
	db = anodb.DB('sqlite', '', 'test-anodb.sql')
	assert db is not None
	db.create_foo()
	assert db.count_foo()[0][0] == 0
	db.insert_foo(pk=1, val='one')
	assert db.count_foo()[0][0] == 1
	db.insert_foo(pk=2, val='two')
	db.commit()
	assert db.count_foo()[0][0] == 2
	assert re.search(r'two', db.select_foo_pk(2)[0][0])
	db.update_foo_pk(pk=2, val='deux')
	db.delete_foo_pk(pk=1)
	db.commit()
	assert db.count_foo()[0][0] == 1
	assert re.search(r'deux', db.select_foo_pk(2)[0][0])
	db.delete_foo_all()
	db.commit()
	assert db.count_foo()[0][0] == 0
	db.insert_foo(pk=3, val='three')
	assert db.count_foo()[0][0] == 1
	db.rollback()
	assert db.count_foo()[0][0] == 0
	db.drop_foo()
	db.commit()
	db.close()
	db.connect()
	db.drop_foo()
	db.close()
