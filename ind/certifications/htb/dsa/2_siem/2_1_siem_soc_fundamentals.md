# SIEM & SOC Fundamentals

- `SOC Director`: Responsible for overall management and
  strategic planning of the SOC, including budgeting, staffing, and
  alignment with organizational security objectives.
- `SOC Manager`: Oversees day-to-day operations, manages the team, coordinates incident response efforts, and ensures smooth
  collaboration with other departments.
- `Tier 1 Analyst`: Monitors security alerts and events,
  triages potential incidents, and escalates them to higher tiers for
  further investigation. Also known as "first responders," these analysts monitor security events and alerts, perform initial triage, and escalate potential incidents to higher tiers for further investigation. Their main goal is to quickly identify and prioritize security incidents.
- `Tier 2 Analyst`: Performs in-depth analysis of escalated
  incidents, identifies patterns and trends, and develops mitigation
  strategies to address security threats. These analysts are more experienced and perform deeper analysis of escalated incidents. They identify patterns and trends, develop mitigation strategies, and sometimes assist in incident response efforts. They may also be responsible for tuning security monitoring tools to reduce false positives and improve detection capabilities.
- `Tier 3 Analyst`: Provides advanced expertise in handling
  complex security incidents, conducts threat hunting activities, and
  collaborates with other teams to improve the organization's security
  posture. Often considered the most experienced and knowledgeable analysts on the team, Tier 3 analysts handle the most complex and high-profile security incidents. They may also engage in proactive threat hunting, develop advanced detection and prevention strategies, and collaborate with other teams to improve the organization's overall security posture.
- `Detection Engineer`: A Detection Engineer is responsible
  for developing, implementing, and maintaining detection rules and
  signatures for security monitoring tools, such as SIEM, IDS/IPS, and EDR solutions. They work closely with security analysts to identify gaps in detection coverage and continuously improve the organization's ability
  to detect and respond to threats.
- `Incident Responder`: Takes charge of active security
  incidents, carries out in-depth digital forensics and containment and
  remediation efforts, and collaborates with other teams to restore
  affected systems and prevent future occurrences.
- `Threat Intelligence Analyst`: Gathers, analyzes, and
  disseminates threat intelligence data to help SOC team members better
  understand the threat landscape and proactively defend against emerging
  risks.
- `Security Engineer`: Develops, deploys, and maintains
  security tools, technologies, and infrastructure, and provides technical expertise to the SOC team.
- `Compliance and Governance Specialist`: Ensures that the
  organization's security practices and processes adhere to relevant
  industry standards, regulations, and best practices, and assists with
  audit and reporting requirements.
- `Security Awareness and Training Coordinator`: Develops
  and implements security training and awareness programs to educate
  employees about cybersecurity best practices and promote a culture of
  security within the organization.

### SOC Stages

1.0 - Organizations invested in certain security layers such as security intelligence platforms or identity management systems. However, the lack of proper integration led to uncorrelated alerts and a buildup of tasks across multiple platforms. This stage was characterized by an emphasis on network and perimeter security, even as threats began exploiting other vectors

2.0 - Built on intelligence, integrating security telemetry, threat intelligence, network flow analysis, and other anomaly detection techniques. Additionally, layer-7 analysis is employed at this stage to identify low and slow attacks and other hidden threats. A forward-looking approach to threat research and collaboration between SOCs, either within sectors or at the national level, is crucial for SOC 2.0's success. Emphasis is placed on complete situational awareness, pre-event preparedness through vulnerability management, configuration management, and dynamic risk management, as well as post-event analysis and learning through incident response and in-depth forensics. Refining security intelligence rules and deploying countermeasures are also vital in this stage.

Cognitive SOC - Takes 2.0 and makes it more efficient, work better together, cleans up the operations and processes and makes it function well in a business

# MITRE

The [MITRE ATT&CK](https://attack.mitre.org/) (Adversarial Tactics, Techniques, and Common Knowledge) framework
serves as an extensive, regularly updated resource outlining the
tactics, techniques, and procedures (TTPs) employed by cyber threat
actors.
