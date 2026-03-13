print("===== CORPORATE FACILITY INFILTRATION SIMULATOR =====")

role = input("Role (employee/contractor/external): ").lower()
access_card = input("Access Card (valid/expired/none): ").lower()
biometric = input("Biometric Scan (match/mismatch/failure): ").lower()
time_of_day = input("Time (day/night/restricted): ").lower()
department = input("Department (it/hr/finance/rnd/security): ").lower()
clearance = input("Clearance (low/mid/high/topsecret): ").lower()
stress_level = input("Stress Level (stable/nervous/panicked): ").lower()
ai_alert = input("AI Alert Level (green/yellow/red): ").lower()
camera_status = input("Camera Status (active/down/hacked): ").lower()
network_status = input("Network (stable/slow/isolated): ").lower()
intent = input("Intent (work/audit/extract/sabotage): ").lower()

print("\n===== SIMULATION START =====")

# LEVEL 1
if role == "employee":

    # LEVEL 2
    if access_card == "valid":

        # LEVEL 3
        if biometric == "match":

            # LEVEL 4
            if time_of_day == "day":

                # LEVEL 5
                if clearance in ["mid", "high", "topsecret"]:

                    # LEVEL 6
                    if department == "rnd":

                        # LEVEL 7
                        if ai_alert == "green":

                            # LEVEL 8
                            if camera_status == "active":

                                # LEVEL 9
                                if network_status == "stable":

                                    # LEVEL 10
                                    if intent == "work":

                                        # LEVEL 11
                                        if stress_level == "stable":

                                            # LEVEL 12
                                            if clearance == "topsecret":

                                                # LEVEL 13
                                                if department == "rnd":

                                                    # LEVEL 14
                                                    if ai_alert == "green":

                                                        # LEVEL 15
                                                        if camera_status == "active":
                                                            print("ACCESS GRANTED: Research Vault Entry")
                                                        elif camera_status == "down":
                                                            print("Security anomaly logged")
                                                        else:
                                                            print("Camera breach detected")

                                                    elif ai_alert == "yellow":
                                                        print("Restricted due to AI anomaly")
                                                    else:
                                                        print("Lockdown triggered")

                                                elif department == "finance":
                                                    print("Cross-department clearance required")
                                                else:
                                                    print("Department mismatch")

                                            elif clearance == "high":
                                                print("Partial vault access")
                                            elif clearance == "mid":
                                                print("Standard research access")
                                            else:
                                                print("Insufficient clearance")

                                        elif stress_level == "nervous":
                                            print("Behavior flagged for monitoring")
                                        else:
                                            print("Security escort assigned")

                                    elif intent == "audit":
                                        print("Audit trail initiated")
                                    elif intent == "extract":
                                        print("Data extraction requires supervisor approval")
                                    else:
                                        print("Sabotage suspicion triggered")

                                elif network_status == "slow":
                                    print("Limited system sync")
                                else:
                                    print("Isolated network: manual override needed")

                            elif camera_status == "down":
                                print("Security notified: blind spot")
                            else:
                                print("Camera tampering alert")

                        elif ai_alert == "yellow":
                            print("Movement logged under watchlist")
                        else:
                            print("AI lockdown active")

                    elif department == "finance":

                        if clearance in ["high", "topsecret"]:

                            if intent == "audit":

                                if ai_alert == "green":

                                    if network_status == "stable":

                                        if stress_level == "stable":

                                            if camera_status == "active":

                                                if time_of_day == "day":

                                                    if biometric == "match":

                                                        if access_card == "valid":

                                                            if role == "employee":

                                                                if department == "finance":

                                                                    if clearance == "topsecret":

                                                                        if ai_alert == "green":

                                                                            if network_status == "stable":
                                                                                print("Financial Core Access Granted")
                                                                            elif network_status == "isolated":
                                                                                print("Manual Audit Mode")
                                                                            else:
                                                                                print("Delayed Access")

                                                                        elif ai_alert == "yellow":
                                                                            print("Supervisor Confirmation Required")
                                                                        else:
                                                                            print("Lockdown")

                                                                    elif clearance == "high":
                                                                        print("Audit Read-Only Mode")
                                                                    else:
                                                                        print("Mid-level Audit")

                                                                else:
                                                                    print("Department mismatch")

                                                            else:
                                                                print("Role escalation denied")

                                                        else:
                                                            print("Card invalid")

                                                    else:
                                                        print("Biometric mismatch")

                                                else:
                                                    print("After-hours restriction")

                                            else:
                                                print("Camera anomaly")

                                        else:
                                            print("Psychological anomaly flagged")

                                    else:
                                        print("Network compromised")

                                else:
                                    print("AI alert blocks audit")

                            else:
                                print("Finance access denied for non-audit intent")

                        else:
                            print("Finance clearance insufficient")

                    else:
                        print("Department access general")

                else:
                    print("Clearance too low")

            elif time_of_day == "night":

                if clearance == "topsecret":

                    if ai_alert == "green":

                        if camera_status == "active":

                            if intent == "work":

                                if stress_level == "stable":

                                    if network_status == "stable":

                                        if department == "security":

                                            if biometric == "match":

                                                if access_card == "valid":

                                                    if role == "employee":

                                                        if clearance == "topsecret":

                                                            if ai_alert == "green":

                                                                if camera_status == "active":

                                                                    if network_status == "stable":

                                                                        if intent == "work":

                                                                            if stress_level == "stable":

                                                                                if department == "security":
                                                                                    print("Night Command Override Activated")

                                                                            elif stress_level == "nervous":
                                                                                print("Monitoring Enabled")
                                                                            else:
                                                                                print("Emergency Lockdown")

                                                                        else:
                                                                            print("Night intent mismatch")

                                                                    else:
                                                                        print("Network unstable")

                                                                else:
                                                                    print("Camera anomaly")

                                                            else:
                                                                print("AI Alert escalated")

                                                        else:
                                                            print("Clearance conflict")

                                                    else:
                                                        print("Role mismatch")

                                                else:
                                                    print("Invalid card")

                                            else:
                                                print("Biometric mismatch")

                                        else:
                                            print("Night access limited to security")

                                    else:
                                        print("Network unstable")

                                else:
                                    print("Psychological anomaly")

                            else:
                                print("Night operation restricted")

                        else:
                            print("Camera down")

                    else:
                        print("AI lockdown")

                else:
                    print("Night access denied")

            else:
                print("Restricted time window")

        elif biometric == "mismatch":
            print("Access denied: biometric mismatch")
        else:
            print("Biometric system failure")

    elif access_card == "expired":
        print("Access denied: card expired")
    else:
        print("No access credentials")

elif role == "contractor":
    print("Limited contractor access pathway")
else:
    print("External entity detected – full security escalation")

print("===== SIMULATION END =====")