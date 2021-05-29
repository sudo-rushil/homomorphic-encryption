# Literature Review

Collection of papers and takeaway information therefrom

## Lindell et al., 2019 – Efficient Constant-Round Multi-Party Computation Combining BMR and SPDZ
- MPC allows distrustful parties to compute a joint functionality of their inputs
- Requires privacy, correctness, and independence of inputs
- 12 communication rounds and 3 online thereof – computational improvement
- BMR protocol allows for semi-honest MPC
- Assume some parties are corrupt – testing strategies?

## Chakarov et al., 2019 – Evaluation of the Complexity of Fully Homomorphic Encryption Schemes in Implementations of Programs
- Extension of Gentry-Sahai-Waters scheme
- FHE schemes form a ( + , * ) ring over encrypted data
	- Secure yet inefficient in speed and memory
	- Noise introduction
- SHE schemes which evaluate their own decryption circuits are called "bootstrappable"
- Need to do statistical analysis
- Supported operations
	- Equality check
	- Min or max of values
	- Addition, subtraction, multiplication, division
	- If statements
- Give examples of some simple search, sort, and graph search algorithms

## Masdari et al., 2016 – Comprehensive analysis of the authentication methods in wireless body area networks
- WBAN are sensors that transmit physiological signals to med servers
- Many schemes needed for channel-based authentication
- Once again, needs low overhead
- Look into zero-knolwedge proof protocols

## Tseng et al., 2017 – Homomorphic Encryption Supporting Logical Operations
- Homomorphic encryption makes computational encapsulation of data possible
- Most systems support additive or multiplicative logic; few do binary logic
- Possible value in private cloud computing, electronic voting, private matching
- RSA, ElGamal have multiplicative homomorphism; Paillier is additive
- Needed operations – KeyGen, Encrypt, Decrypt
- Table 4...
- Does not support NOT
- Hardness: subgroup decision problem <- look up

## Hazay et al., 2020 – On the Power of Secure Two-Party Computation
- In one case of MPC, a majority of parties are honest, and in another, any number may be adversarial
- Zero-knowledge protocol: allow prover to convince verifier of a validity of a statement with no additional knowledge
- ZK is equivalent to semi-honest 2PC
- MPC normally achieved by garbled circuits

## Bitansky, 2017 – Verifiable Random Functions from Non-interactive Witness-Indistinguishable Proofs
- VRFs are pseudorandom functions that allow encrypted verification of output
- Basis for indistinguishability obfuscation
- Need key sampler, prover, and verifier
- Proof of hardness: witness indistinguishability

## Beimel et al., 2020 – 1/p-Secure Multiparty Computation without an Honest Majority and the Best of Both Worlds
- Protocol is secure if an adversary cannot cause more harm than in the ideal case – fairness impossible without honest majority
- 1/p protocols are resilient against adversarial MPC setups
- Similar background to coin-tossing protocols
- Are there general multiparty 1/p secure and private protocols?
- In MPC, all comunications are all a signle channel
	- Can avoid practically with single ideal bidirectional channel

## Halevi et al., 2021 – Round-Optimal Secure Multi-party Computation
- Identification of round complexity for arbitrary secure computations
- Hardness: decisional Diffie-Hellman, LWE
- Note: state a theorem in sec. 1 that the paper will end by proving
- Additive errors still exist in BMR
- Achieve MPC in 4 rounds (sec. 1.2.2)

## Ateniese et al., 2021 – Match Me if You Can: Matchmaking Encryption and Its Applications
- Based on dead drop key exchange – new paradigm
- Sender can specify arbitrary policy the receiver must satisfy
	- Trusted authority protects sender attributes from spoofing
- Note: along with applications, give analogous scenario

## Brakerski et al., 2011 – Fully Homomorphic Encryption without Bootstrapping
- Leveled FHE is O(lambda x L3)
- Solving FHE schemes tractably requires denoising repeated bootstrapping circuits
- Per-gate computation is greatest overhead
- Hardness: learning with errors problem