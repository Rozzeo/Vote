from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

# Генерация ключей для избирателя
def generate_voter_keys():
    private_key = RSA.generate(2048)
    public_key = private_key.publickey()
    return private_key, public_key и 

# Симуляция регистрации избирателя и получение "права голоса"
voter_private_key, voter_public_key = generate_voter_keys()

# Генерация голоса
vote = "Democrat"

# Создание подтверждения права голоса (нулевое доказательство)
def generate_vote_proof(voter_private_key, vote):
    message = vote.encode()
    hash_message = SHA256.new(message)
    signature = pkcs1_15.new(voter_private_key).sign(hash_message)
    return vote, signature

# Проверка подтверждения права голоса (без раскрытия голоса)
def verify_vote_proof(voter_public_key, vote, signature):
    message = vote.encode()
    hash_message = SHA256.new(message)
    try:
        pkcs1_15.new(voter_public_key).verify(hash_message, signature)
        return True
    except (ValueError, TypeError):
        return False

# Голосование и проверка подтверждения права голоса
vote, signature = generate_vote_proof(voter_private_key, vote)
is_valid = verify_vote_proof(voter_public_key, vote, signature)

if is_valid:
    print("Голос действителен.")
else:
    print("Голос недействителен.")

