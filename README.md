# How To Prevent Denial Of Service By Refusing To Accept Ether
1. Inside our contract folder we have three contracts the KingOfEther, Attack and FixedKingOfEther contract.
2. Our kingOfEther contract allows users to deposit ether to become the new king of the contract overthrowing the previous king by depositing a higher amount
3. The contract is vulnerable to denial of service when its called by the attack contract, this is because the attack contract doesnt have any form of fallback function to receive ether.
4. Check out the FixedKingOfEther and see how we fixed the contract up!(We could have also fixed this using the pull method rather than push)
5. Oh! and if you're interested in the tests and scripts for the contract check the scripts and test folders respectively!( Brownie ;) )
6. Hopefully you learnt something new!. Bless!
7. Let's connect on twitter @FranFran_E