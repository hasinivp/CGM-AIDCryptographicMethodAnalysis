## System Description  
  
CGM/AID systems are commonly used among the diabetic population globally. This system works to take continuous glucose readings from the CGM device to then use algorithms in the controller device to determine the correct insulin dosage - which is then given to the patient accordingly.__

While there are multiple hardware architectures of these systems, I have outlined the most common one (where the central controller is embedded as firmare in the Insulin Pump) below:

```text
+----------------+
|   CGM Sensor   |
+----------------+

      |
	  |  (Encrypts glucose readings every 1-5 mins through BLE)
	  V
+----------------+
| Insulin Pump   |                                                           +------------+
| + embedded     |  ----> (Uses chip+algorithms to determine insulin dosage) |  Patient   |
| firmware chip  |                                                           +------------+
+----------------+
      
      |
	  |  (Sends readings/data to phone through BLE)
	  V
+---------------+
| Mobile Device | ----> (Mobile often will often have override access to pump)
+---------------+
```


---  
  
## Assets  
    
- Medical data  
- PHI  
- Access to potentially harm patient  
  
---  
  
## Threat Actors  
  
- External attackers  
- Cybercriminals  
  
---  
  
## Entry Points  
  
The attacker has multiple entry points. The most prevelant are the BLE connection from the CGM to isulin pump, the BLE connection from the pump to the smartphone/mobile device, or the mobile device itself.  
---  
