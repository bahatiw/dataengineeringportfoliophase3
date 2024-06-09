db = db.getSiblingDB('admin');
db.auth('bahati', 'bahati');

db = db.getSiblingDB('farmers');
db.createUser({
  user: 'bahati2',
  pwd: 'bahati2',
  roles: [
    {
      role: 'readWrite',
      db: 'farmers',
    },
  ],
});

db.createCollection('test_farmers');