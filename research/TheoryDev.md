# Theory Development

Record of development of theoretical underpinnings of cryptosystem

## May 28, 2021

Definitions:
- Homomorphic system: encrypted data supports computation
- Multi-party system: adversarial users can aggregate encrypted data
- Matchmaking system: dead-drop key exchange

## May 31, 2021

Goals for system:
- Support two-person encryption
- Develop biomimetic algorithms for paired encryption
	- E.g. utilize the image of protein folding as a to-be-reduced NP-complete problem for an uninvertable lock
	- https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2443096/
- Be fast, and easy to implement
- Demo w/ Streamlit

## June 1, 2021

RSA System – asymmetric:
- Setup:
	- Private: p, q, d; public: n, e
	- Pick large primes p, q
	- n = pq
	- ϕ(n) = (p-1)(q-1)
	- Pick e s.t. gcd(e, ϕ(n)) = 1
	- d = e^-1 (mod ϕ(n)) – d is modular inverse of e
- Use:
	- Bob wants to send message m to Alice
	- Sends M = m^e
	- Alice computes M^d = m^ed = m^(1+kϕ(n)) = m (mod n)
		- Recall de = 1 (mod ϕ(n))
	- Alice now has m
- Trapdoor is discrete logarithm – given M, e, and n, computing m s.t. m^e = M (mod n) is hard

Type View of Cryptography:
- Homomorphic Encryption:
	- 