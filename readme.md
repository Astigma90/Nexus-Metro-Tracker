# Nexus Metro Tracker

Nexus Metro Tracker uses Nexus' public APIs to get up-to-date information from any station on the Tyne and Wear Metro.

## Usage

Run the script with Python and enter one of the station codes to see the latest information available

```bash
python metro.py

# Returns station codes

Available Stations:
APT: Airport
BDE: Bede
BFT: Bank Foot
BTN: Benton
BYK: Byker
BYW: Brockley Whins
CAL: Callerton Parkway
CEN: Central Station
CHI: Chichester
CRD: Chillingham Road
CUL: Cullercoats
EBO: East Boldon
FAW: Fawdon
FEL: Felling
FGT: Fellgate
FLE: Four Lane Ends
GHD: Gateshead
GST: Gateshead Stadium
HAY: Haymarket
HDR: Hadrian Road
HEB: Hebburn
HOW: Howdon
HTH: Heworth
ILF: Ilford Road
JAR: Jarrow
JES: Jesmond
KSP: Kingston Park
LBN: Longbenton
MAN: Manors
MLF: Millfield
MSN: Monkseaton
MSP: St Peter\'s
MTS: Monument N-S
MTW: Monument W-E
MWL: Meadow Well
NPK: Northumberland Park
NSH: North Shields
PAL: Pallion
PCM: Percy Main
PLI: Park Lane
PLW: Pelaw
PMV: Palmersville
RGC: Regent Centre
SBN: Seaburn
SFC: Stadium of Light
SGF: South Gosforth
SHL: South Hylton
SJM: St James
SMD: Simonside
SMR: Shiremoor
SSS: South Shields
SUN: Sunderland
TDK: Tyne Dock
TYN: Tynemouth
UNI: University
WBR: Wansbeck Road
WJS: West Jesmond
WKG: Walkergate
WMN: West Monkseaton
WSD: Wallsend
WTL: Whitley Bay
Enter station code: MTS

# Returns platform information

Enter station code: MTS

Platform 1:
==================================================
Train 131 (YELLOW Line) to South Shields
  Status: ARRIVED at West Jesmond Platform 1 (2025-03-04T19:51:11.0000000+00:00)
  Due in: 6 minutes
  Scheduled: 2025-03-04T19:53:15.0000000+00:00 | Predicted: 2025-03-04T19:57:46.0000000+00:00
--------------------------------------------------
Train 101 (GREEN Line) to South Hylton
  Status: DEPARTED at Regent Centre Platform 1 (2025-03-04T19:50:18.0000000+00:00)
  Due in: 10 minutes
  Scheduled: 2025-03-04T20:01:15.0000000+00:00 | Predicted: 2025-03-04T20:01:53.0000000+00:00
--------------------------------------------------
Train 132 (YELLOW Line) to South Shields
  Status: DEPARTED at Northumberland Park Platform 1 (2025-03-04T19:51:21.1550000+00:00)
  Due in: 18 minutes
  Scheduled: 2025-03-04T20:08:15.0000000+00:00 | Predicted: 2025-03-04T20:10:02.0000000+00:00
--------------------------------------------------
Train 133 (YELLOW Line) to South Shields
  Status: DEPARTED at Tynemouth Platform 1 (2025-03-04T19:51:25.8640000+00:00)
  Due in: 31 minutes
  Scheduled: 2025-03-04T20:23:15.0000000+00:00 | Predicted: 2025-03-04T20:22:58.0000000+00:00
--------------------------------------------------

Platform 2:
==================================================
Train 105 (GREEN Line) to Airport
  Status: DEPARTED at Gateshead Platform 2 (2025-03-04T19:50:59.0000000+00:00)
  Due in: 3 minutes
  Scheduled: 2025-03-04T19:47:15.0000000+00:00 | Predicted: 2025-03-04T19:54:17.0000000+00:00
--------------------------------------------------
Train 126 (YELLOW Line) to St James
  Status: DEPARTED at Gateshead Stadium Platform 2 (2025-03-04T19:51:17.0000000+00:00)
  Due in: 5 minutes
  Scheduled: 2025-03-04T19:54:15.0000000+00:00 | Predicted: 2025-03-04T19:56:23.0000000+00:00
--------------------------------------------------
Train 106 (GREEN Line) to Airport
  Status: APPROACHING at Pelaw Junction Platform 1 (2025-03-04T19:51:09.7340000+00:00)
  Due in: 13 minutes
  Scheduled: 2025-03-04T20:02:15.0000000+00:00 | Predicted: 2025-03-04T20:04:14.0000000+00:00
--------------------------------------------------
Train 127 (YELLOW Line) to St James
  Status: APPROACHING at Jarrow Platform 2 (2025-03-04T19:51:08.9560000+00:00)
  Due in: 18 minutes
  Scheduled: 2025-03-04T20:09:15.0000000+00:00 | Predicted: 2025-03-04T20:09:50.0000000+00:00

```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
