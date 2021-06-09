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
- Difficulty is prime factorization problem – finding ϕ(n) is all that is needed to retrieve d, but this is impossible
- Trapdoor is discrete logarithm – given M, e, and n, computing m s.t. m^e = M (mod n) is hard
	- Note, this is actually difficulty with Diffie-Hellman

## June 2, 2021

Type View of Cryptography:
- RSA:
	- Prep :: { p : prime } -> { q : prime } -> ({ n : int }, { e : int }, { d : int })
	- Encrypt :: { m : int } -> { e : int } -> { n : int } -> { M : int }
	- Decrypt :: { M : int } -> { d : int } -> { n : int } -> { m : int }
- Homomorphic Encryption:
	- Encrypt :: a -> k -> S a k
	- Compute :: (a -> b) -> S a k -> S b k
		- Note, this is just <$>
		- Functor, not Monad
	- Decrypt :: k -> S a k -> a
- MPC:
	- Encrypt :: a -> S a
	- Combine :: [S a] -> ([a] -> b) -> b
	- Note: there is NO way to "decrypt" an encrypted value

System Brainstorming:
- Comparisons of values before and after encryption should be same
- Working from encrypted to plaintext value should be impossible
	- Only original holder should know their value

## June 3, 2021

System Brainstorming:
- System of input numbers x,y \in Z/nZ, and encryption function e
- Have that two orthogonal values remain orthogonal, but no other
	- if (x,y)=1, then (e(x),e(y)) = 1, but it is *not* true that (x,y)=(e(x),e(y)) in general
		- Such a condition would imply an orthogonal transformation, which is easily invertable
- Pick N, e, and d as in RSA
- Encrypt – X = x^e, Y = y^e
- Then, X x Y = 1 iff xy = 1, but X and Y *cannot* be worked back into x and y!
- Decrypt – X^d, or Y^d

Explanation:
- Why is it sufficient for us to only check whether two numbers are modular inverses?
	- Because any behavior can be encoded as such!
	- E.g. if (a,b) matches in R then there will be a mapping into a space where (a',b')=1
- Need mapping from 2^k -> Z/nZ
	- Constructable in initialization of system
	- Can support N/2 unique pairs at most

To Implement:
- Example mapping from problem space to Z/nZ space
	- Function documentation!
- Encryption algorithm

## June 4, 2021

Paper Structure:
- Introduction
- Theory – Algorithm, Proof of Correctness, Proof of Reducability to Strong RSA
- Discussion – Python code, performance benchmarks, examples, Reflect on performance, ease of implementation, and 
- Conclusion