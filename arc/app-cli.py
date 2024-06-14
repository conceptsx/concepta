import random
import os
import sys

questions = [
    ("What does 'a' mean?", ["before", "after", "around"], "a"),
    ("What does 'A' stand for?", ["assist", "assessment data", "active"], "b"),
    ("What does 'AA' mean?", ["assistive device", "active", "active assist"], "c"),
    ("What does 'AAROM' stand for?", ["active range of motion", "active assistive range of motion", "assisted range of motion"], "b"),
    ("What does 'abd' stand for?", ["abduction", "adduction", "abnormal"], "a"),
    ("What does 'ABI' stand for?", ["abnormal", "acquired brain injury", "assistive device"], "b"),
    ("What does 'a.c.' mean?", ["before meals", "after meals", "around meals"], "a"),
    ("What does 'ACA' stand for?", ["anterior cerebral artery", "American College of Cardiology", "Affordable Care Act"], "c"),
    ("What does 'AC joint' mean?", ["anterior cervical joint", "acromioclavicular joint", "anterior cruciate joint"], "b"),
    ("What does 'ACCE' stand for?", ["Academic Coordinator of Clinical Education", "anterior cruciate ligament", "anterior cerebral artery"], "a"),
    ("What does 'ACL' stand for?", ["anterior cervical ligament", "anterior cruciate ligament", "anterior cerebral ligament"], "b"),
    ("What does 'AD' stand for?", ["Assistive Device", "American with Disabilities Act", "American Diabetes Association"], "a"),
    ("What does 'ADA' stand for?", ["American with Disabilities Act", "American Dental Association", "American Diabetes Association"], "a"),
    ("What does 'add.' mean?", ["adduction", "addition", "abduction"], "a"),
    ("What does 'ADL' stand for?", ["activities of daily living", "assistive device", "active daily living"], "a"),
    ("What does 'ad lib' mean?", ["at discretion", "as needed", "at liberty"], "a"),
    ("What does 'AE' mean?", ["above elbow", "below elbow", "ankle extension"], "a"),
    ("What does 'AFO' stand for?", ["anterior foot orthoses", "ankle foot orthoses", "anterior cruciate ligament"], "b"),
    ("What does 'AIIS' stand for?", ["anterior inferior iliac spine", "anterior ilium inferior spine", "anterior iliac inferior spine"], "a"),
    ("What does 'A/K' mean?", ["around knee", "above knee", "ankle/knee"], "b"),
    ("What does 'AKA' stand for?", ["above knee amputation", "anterior knee arthroplasty", "ankle knee arthroplasty"], "a"),
    ("What does 'AKS' mean?", ["anterior knee surgery", "arthroscopic knee surgery", "arthroplasty knee surgery"], "b"),
    ("What does 'AKFO' stand for?", ["ankle knee fixation orthosis", "ankle knee foot orthosis", "ankle knee foot orthoses"], "b"),
    ("What does 'AMA' mean?", ["against medical advice", "American Medical Association", "American with Disabilities Act"], "a"),
    ("What does 'amb' mean?", ["ambulation", "ambulance", "ambulation device"], "a"),
    ("What does 'amt' mean?", ["amount", "amputation", "ambulation"], "a"),
    ("What does 'ant' mean?", ["anterolateral", "anterior", "anteroposterior"], "b"),
    ("What does 'ante' mean?", ["before", "after", "around"], "a"),
    ("What does 'AOTA' stand for?", ["American Occupational Therapy Association", "American Osteopathic Therapy Association", "American Orthopedic Therapy Association"], "a"),
    ("What does 'A-P' stand for?", ["anterior-posterior", "anteroposterior", "anterior-proximal"], "b"),
    ("What does 'appt' stand for?", ["appointment", "appropriate", "approximate"], "a"),
    ("What does 'APTA' stand for?", ["American Physical Therapy Association", "American Physical Training Association", "American Physiotherapy Association"], "a"),
    ("What does 'AROM' stand for?", ["active range of motion", "active range of movement", "assistive range of motion"], "a"),
    ("What does 'ASAP' mean?", ["as soon as possible", "as shortly as possible", "at soon as possible"], "a"),
    ("What does 'ASHA' stand for?", ["American Speech Language Hearing Association", "American Speech and Language Association", "American Speech and Hearing Association"], "a"),
    ("What does 'ASIS' stand for?", ["anterior superior iliac spine", "anterior spine iliac segment", "anterior spine iliac support"], "a"),
    ("What does 'assist.' stand for?", ["assistant", "assistance", "assistantship"], "b"),
    ("What does 'ATNR' stand for?", ["asymmetrical tonic neck reflex", "asymmetrical tonic neural reflex", "asymmetrical tonic neurological response"], "a"),
    ("What does 'ax. cr' stand for?", ["axial crutches", "axial crotch", "axillary crutches"], "c"),
    ("What does 'B' stand for?", ["bilateral fracture", "both", "bilateral"], "b"),
    ("What does 'BBFA' stand for?", ["both bone forearm fractures", "bilateral forearm fractures", "bilateral bone forearm fractures"], "a"),
    ("What does 'b/c' mean?", ["because", "before", "between"], "a"),
    ("What does 'BE' mean?", ["before elbow", "below elbow", "below elbow joint"], "b"),
    ("What does 'bid' mean?", ["twice a day", "twice daily", "twice in a day"], "a"),
    ("What does 'bil.' stand for?", ["bilateral limbs", "bilateral", "bilateral arms"], "b"),
    ("What does 'biw' mean?", ["bi-weekly therapy", "bi-weekly", "twice a week"], "c"),
    ("What does 'B/K' mean?", ["below knee joint", "below knee", "below knee amputation"], "b"),
    ("What does 'BKA' stand for?", ["below knee alignment", "below knee amputation", "below knee arthroplasty"], "b"),
    ("What does 'BLE' stand for?", ["both lower extremities", "bilateral lower extremities", "below lower extremities"], "a"),
    ("What does 'BMI' stand for?", ["body muscle index", "body mass index", "body metabolic index"], "b"),
    ("What does 'BOS' stand for?", ["base of support", "base of spine", "basis of support"], "a"),
    ("What does 'BP' mean?", ["blood pressure", "blood pulse", "blood pressure reading"], "a"),
    ("What does 'bpm' mean?", ["beats per second", "beats per minute", "beats per moment"], "b"),
    ("What does 'BUE' stand for?", ["both upper extremities joints", "bilateral upper extremities", "both upper extremities"], "c"),
    ("What does 'BR' stand for?", ["bedroom rest", "bedroom", "bedrest"], "c"),
    ("What does 'B/S' stand for?", ["beside support", "bedside", "beside"], "b"),
    ("What does 'c' mean?", ["with", "without", "concerning"], "a"),
    ("What does 'CAPTE' stand for?", ["Commission on Physical Therapy Education", "Commission on Accreditation of Physical Therapy Education", "Commission on Accreditation in Physical Therapy Education"], "c"),
    ("What does 'CARF' stand for?", ["Commission on Rehabilitation Facilities", "Commission on Accreditation of Rehabilitation Facilities", "Commission on Accreditation of Rehab Facilities"], "b"),
    ("What does 'CC' stand for?", ["chief concern", "chief condition", "chief complaint"], "c"),
    ("What does 'cc' stand for?", ["centimeter cubed", "cubic centimeter", "cubic centimeters"], "b"),
    ("What does 'CCCE' stand for?", ["Coordinator of Clinical Education", "Center Coordinator of Clinical Education", "Center Coordinator for Clinical Education"], "b"),
    ("What does 'C & DB' stand for?", ["cough and deep breaths exercises", "cough and deep breathing", "cough and deep breaths"], "b"),
    ("What does 'CGA' stand for?", ["contact guard assistance", "contact guard assist", "contact guard assistive"], "b"),
    ("What does 'CHD' stand for?", ["congenital heart disease", "congenital heart defect", "congenital heart disorder"], "a"),
    ("What does 'CHI' stand for?", ["closed head injury", "closed head infection", "closed head incident"], "a"),
    ("What does 'CI' stand for?", ["Clinical Instructor Coordinator", "Clinical Instructive", "Clinical Instructor"], "c"),
    ("What does 'CiTx' stand for?", ["cervical intermittent traction", "cervical intensive traction", "cervical intervertebral traction"], "a"),
    ("What does 'cm' mean?", ["centimeters", "centimeter", "cubic meter"], "a"),
    ("What does 'c/o' mean?", ["complains of", "concerning", "complaints of"], "a"),
    ("What does 'COG' mean?", ["center of gravity point", "center of gravity", "cognitive orientation"], "b"),
    ("What does 'coord' mean?", ["coordinator", "coordination", "coordination movement"], "b"),
    ("What does 'CP' mean?", ["cranial palsy", "compression pump", "cerebral palsy"], "c"),
    ("What does 'CPM' stand for?", ["controlled passive motion", "continuous passive motion", "continuous positive movement"], "b"),
    ("What does 'CMS' stand for?", ["Centers for Medicaid Services", "Centers for Medicare & Medicaid Services", "Centers for Medicare Services"], "b"),
    ("What does 'CN' mean?", ["cranial nerve", "central nerve", "cervical nerve"], "a"),
    ("What does 'cont' mean?", ["continual", "continued", "continue"], "c"),
    ("What does 'CORF' stand for?", ["Comprehensive Outpatient Rehab Facility", "Comprehensive Outpatient Rehabilitation Facility", "Comprehensive Outpatient Rehabilitation Fund"], "b"),
    ("What does 'COTA' stand for?", ["certified occupational therapist assistant", "certified occupational therapy assistant", "certified occupational therapist aide"], "b"),
    ("What does 'CPR' stand for?", ["cardiopulmonary rehabilitation", "cardiopulmonary resuscitation", "cardiopulmonary recovery"], "b"),
    ("What does 'CPT' stand for?", ["chest PT", "chest procedural terminology", "current procedural terminology"], "c"),
    ("What does 'CRA' stand for?", ["Certified Rehabilitation Agency", "Certified Rehab Aide", "Certified Rehab Agency"], "a"),
    ("What does 'CRF' stand for?", ["chronic renal failure", "cranial renal failure", "cerebral renal failure"], "a"),
    ("What does 'CSF' stand for?", ["central spinal fluid", "cerebral spinal fluid", "cranial spinal fluid"], "b"),
    ("What does 'CT scan' stand for?", ["computed tomography", "computed axial tomography", "central axial tomography"], "a"),
    ("What does 'CVA' stand for?", ["cervical vascular accident", "cranial vascular accident", "cerebral vascular accident"], "c"),
    ("What does 'CW' mean?", ["continuous wave", "central wave", "cranial wave"], "a"),
    ("What does 'CX' mean?", ["consult", "cancel", "continued"], "b"),
    ("What does 'c/w' mean?", ["consistent with", "concerning with", "correlating with"], "a"),
    ("What does 'd/c' mean?", ["discontinued", "discharged", "disconnected"], "a"),
    ("What does 'DEP' mean?", ["data, evaluation, progress", "data, evaluation, performance goals", "data, evaluation, procedures"], "b"),
    ("What does 'Dept' stand for?", ["depot", "department", "deposition"], "b"),
    ("What does 'DIP' stand for?", ["distal interphalangeal fracture", "distal interphalangeal joint", "distal interphalangeal"], "b"),
    ("What does 'DF' mean?", ["dorsiflexion", "dorsiflexion fracture", "distal fracture"], "a"),
    ("What does 'DJD' stand for?", ["degenerative joint disorder", "degenerative joint disease", "degenerative joint dysfunction"], "b"),
    ("What does 'DME' stand for?", ["durable medical emergency", "durable medical equipment", "durable medical evaluation"], "b"),
    ("What does 'DNR' stand for?", ["do not return", "do not revive", "do not resuscitate"], "c"),
    ("What does 'DOA' mean?", ["date of admission", "date of assessment", "dead on arrival"], "c"),
    ("What does 'DOB' mean?", ["date of baseline", "date of birth", "date of biopsy"], "b"),
    ("What does 'DOD' mean?", ["date of discharge", "date of diagnosis", "date of death"], "c"),
    ("What does 'DPT' stand for?", ["Doctor of Physiotherapy", "Doctor of Physical Therapy", "Doctor of Physical Training"], "b"),
    ("What does 'drsg' mean?", ["diagnosis", "dressing", "drug"], "b"),
    ("What does 'DRGs' stand for?", ["Diagnosis-Related Grading", "Diagnosis-Related Groups", "Diagnosis-Related Goals"], "b"),
    ("What does 'DTR' stand for?", ["deep tendon reflex", "deep tendon response", "deep tendon reaction"], "a"),
    ("What does 'DSD' mean?", ["dry sterile diagnosis", "dry sterile dressing", "dry sterile drug"], "b"),
    ("What does 'DVT' stand for?", ["deep vein thrombosis", "deep vascular thrombosis", "deep venous thrombosis"], "c"),
    ("What does 'Dx' stand for?", ["diagnosis", "drug", "discharge"], "a"),
    ("What does 'ECF' stand for?", ["extended care family", "extended care facility", "extended care fund"], "b"),
    ("What does 'Elec.' mean?", ["electric", "electronics", "electrical"], "c"),
    ("What does 'EMG' stand for?", ["electromyogram", "electromyography", "electromyograph"], "a"),
    ("What does 'EOB' mean?", ["edge of baseline", "edge of bed", "edge of balance"], "b"),
    ("What does 'equip.' stand for?", ["equivalent", "equipment", "equity"], "b"),
    ("What does 'ER' stand for?", ["emergency room", "emergency report", "emergency response"], "a"),
    ("What does 'E.S.' stand for?", ["electrical system", "electrical stimulation", "electrical study"], "b"),
    ("What does 'ex.' mean?", ["execution", "exercise", "examination"], "b"),
    ("What does 'ext.' mean?", ["external", "extreme", "extension"], "c"),
    ("What does 'Ev, ev' stand for?", ["eversion", "evaluation", "evacuation"], "a"),
    ("What does 'Eval' stand for?", ["evaluator", "evaluation", "evasive"], "b"),
    ("What does 'F' mean?", ["fair muscle strength grade", "female", "father"], "b"),
    ("What does 'FAQ' stand for?", ["full arc quadrants", "full arc questions", "full arc quads"], "c"),
    ("What does 'FAROM' stand for?", ["functional active range of movement", "functional active range of motion", "functional active range of monitoring"], "b"),
    ("What does 'FERPA' stand for?", ["Family Educational Rights and Privacy Act", "Family Education Rights and Privacy Act", "Family Educational Rights and Privacy Agreement"], "a"),
    ("What does 'FES' stand for?", ["functional electrical stimulation", "functional electrical study", "functional electrical system"], "a"),
    ("What does 'FIM' stand for?", ["Functional Independence Management", "Functional Independence Measure", "Functional Independence Monitoring"], "b"),
    ("What does 'Flex, ✓' mean?", ["flexibility", "flexion", "flexible"], "b"),
    ("What does 'FLR' stand for?", ["Functional Limitation Response", "Functional Limitation Reporting", "Functional Limitation Record"], "b"),
    ("What does 'FOR' stand for?", ["functional outcome report", "functional outcome record", "functional outcome response"], "a"),
    ("What does 'FRC' stand for?", ["functional residual capacitance", "functional residual capacity", "functional residual care"], "b"),
    ("What does 'FS' stand for?", ["Functional Scale", "Functional Study", "Functional System"], "a"),
    ("What does 'ft' mean?", ["foot", "feet", "feet"], "a"),
    ("What does 'FTP' stand for?", ["failure to progress", "failure to process", "failure to proceed"], "a"),
    ("What does 'FTSG' stand for?", ["full thickness skin graft", "full thickness skin generation", "full thickness skin growth"], "a"),
    ("What does 'F/U' stand for?", ["follow up", "follow under", "follow until"], "a"),
    ("What does 'FWB' stand for?", ["full weight-bearing", "full weight balance", "full weight bearing"], "a"),
    ("What does 'FWW' stand for?", ["front wheel walking", "front-wheel walker", "front-wheel walker"], "b"),
    ("What does 'Fx' stand for?", ["function", "flex", "fracture"], "a"),
    ("What does 'G' mean?", ["great muscle strength", "good muscle strength", "good movement"], "b"),
    ("What does 'GA' stand for?", ["gestational age", "gestational adjustment", "gestational agreement"], "a"),
    ("What does 'gastrocs' mean?", ["gastrocnemius muscles", "gastrocnemius movement", "gastrocnemius moment"], "a"),
    ("What does 'GBS' stand for?", ["Guillain-Barré study", "Guillain-Barré system", "Guillain-Barré syndrome"], "c"),
    ("What does 'GCS' stand for?", ["Glasgow Coma Study", "Glasgow Coma System", "Glasgow Coma Scale"], "c"),
    ("What does 'GI' stand for?", ["gastrointestinal index", "gastrointestinal", "gastrointestinal indicator"], "b"),
    ("What does 'gluts.' mean?", ["gluteals", "gluteus", "gluteal"], "a"),
    ("What does 'gm' mean?", ["grams", "gram", "grammeter"], "b"),
    ("What does 'GMT' stand for?", ["gross muscle testing", "gross muscle test", "gross muscle test"], "b"),
    ("What does 'gt.' mean?", ["gate", "gait", "gait"], "b"),
    ("What does 'GXT' stand for?", ["graded exercise test", "graded exercise testing", "graded exercise test"], "a"),
    ("What does 'H' stand for?", ["husband", "heart", "head"], "a"),
    ("What does 'HBP' stand for?", ["high blood pressure", "high body pressure", "hypertensive blood pressure"], "a"),
    ("What does 'HCFA' stand for?", ["Health Care Financial Administration", "Health Care Funding Association", "Health Care Financing Administration"], "c"),
    ("What does 'h' stand for?", ["hospital", "hour", "hours"], "b"),
    ("What does 'H & P' stand for?", ["history and prognosis", "history and physical", "health and physical"], "b"),
    ("What does 'HA' stand for?", ["headache", "heart attack", "hypertension assessment"], "a"),
    ("What does 'Hemi' stand for?", ["hemisphere", "hemiplegia", "hemiparesis"], "b"),
    ("What does 'HEP' stand for?", ["home exercise program", "home education program", "home evaluation program"], "a"),
    ("What does 'HHA' stand for?", ["home health aide", "home health agent", "home health assistant"], "a"),
    ("What does 'HI' stand for?", ["hip inflammation", "head injury", "heart infection"], "b"),
    ("What does 'HMO' stand for?", ["Health Maintenance Organization", "Health Management Organization", "Home Medical Organization"], "a"),
    ("What does 'HNP' stand for?", ["herniated nucleus pulposus", "hypernatremia", "hernia nerve plexus"], "a"),
    ("What does 'h/o' stand for?", ["health of", "history of", "habit of"], "b"),
    ("What does 'HO' stand for?", ["heterotopic ossification", "hand orthosis", "heart operation"], "a"),
    ("What does 'HOB' stand for?", ["heel of bed", "head of bed", "height of bed"], "b"),
    ("What does 'horiz.' mean?", ["horizontal", "height of residence", "hypotonic"], "a"),
    ("What does 'HP' stand for?", ["hip prosthesis", "hot pack", "heart pump"], "b"),
    ("What does 'HPSO' stand for?", ["Health-care Professional Services Organization", "Health-care Patient Services Organization", "Health-care Provider Services Organization"], "c"),
    ("What does 'HR' stand for?", ["hip rotation", "heart rate", "hospital recovery"], "b"),
    ("What does 'hr' stand for?", ["heart rhythm", "hospital room", "hour"], "c"),
    ("What does 'h.s.' mean?", ["hospital stay", "at bedtime", "health status"], "b"),
    ("What does 'HS' stand for?", ["heel spur", "hamstring", "hip surgery"], "b"),
    ("What does 'ht.' stand for?", ["hip treatment", "height", "home therapy"], "b"),
    ("What does 'HWR' stand for?", ["hardware removal", "home wound recovery", "hip with rotation"], "a"),
    ("What does 'HX' stand for?", ["hemorrhage", "history", "hospital exit"], "b"),
    ("What does 'I' stand for?", ["infection", "independent", "intensive"], "b"),
    ("What does 'ICBG' stand for?", ["iliac crest bone graft", "intracranial bone graft", "internal carotid bone graft"], "a"),
    ("What does 'ICD-9' stand for?", ["International Classification of Diseases, Ninth Revision", "Intracranial Device, Ninth Revision", "Interventional Cardiac Device, Ninth Model"], "a"),
    ("What does 'ICD-10' stand for?", ["International Classification of Diseases, Tenth Revision", "Interventional Cardiac Device, Tenth Model", "Intracranial Device, Tenth Revision"], "a"),
    ("What does 'ICD-11' stand for?", ["International Classification of Diseases, Eleventh Revision", "Intracranial Device, Eleventh Revision", "Interventional Cardiac Device, Eleventh Model"], "a"),
    ("What does 'ICH' stand for?", ["intracranial hyperplasia", "intracranial hemorrhage", "intracranial hypoxia"], "b"),
    ("What does 'ICHI' stand for?", ["Intracranial Classification of Health Interventions", "Internal Classification of Health Interventions", "International Classification of Health Interventions"], "c"),
    ("What does 'ICIDH' stand for?", ["International Classification of Impairments, Disabilities, and Handicaps", "International Classification of Infectious Diseases and Health", "International Classification of Intracranial Disabilities and Handicaps"], "a"),
    ("What does 'ICIDH-2' stand for?", ["International Classification of Infectious Diseases and Health, Second Edition", "International Classification of Functioning and Disability", "International Classification of Intracranial Disabilities and Handicaps, Second Edition"], "b"),
    ("What does 'ICP' stand for?", ["intercostal pressure", "intracranial pressure", "intracardiac pressure"], "b"),
    ("What does 'ICU' stand for?", ["intracranial unit", "intensive care unit", "intensive cardiac unit"], "b"),
    ("What does 'IE' stand for?", ["intermediate evaluation", "initial evaluation", "intracranial evaluation"], "b"),
    ("What does 'I/E ratio' stand for?", ["inspiratory/expiratory ratio", "intercostal/extracardiac ratio", "intracardiac/extracardiac ratio"], "a"),
    ("What does 'IEP' stand for?", ["internal evaluation plan", "individualized education plan", "individual evaluation program"], "b"),
    ("What does 'IFC' stand for?", ["intercostal current", "interferential current", "intracardiac current"], "b"),
    ("What does 'IFSP' stand for?", ["internal family service plan", "individual family service plan", "individual evaluation program"], "b"),
    ("What does 'IM' stand for?", ["intramuscular", "intercostal", "intracardiac"], "a"),
    ("What does 'in.' mean?", ["inches", "inhalation", "inoculation"], "a"),
    ("What does 'inf.' mean?", ["inferior", "infection", "inflammation"], "a"),
    ("What does 'IP' stand for?", ["internal patient", "intracardiac patient", "inpatient"], "c"),
    ("What does 'IPA' stand for?", ["individual practice association", "internal practice association", "individual patient association"], "a"),
    ("What does 'int.' mean?", ["internal", "intercostal", "intramuscular"], "a"),
    ("What does 'IS' stand for?", ["internal spirometer", "incentive spirometer", "intercostal spirometer"], "b"),
    ("What does 'IV' stand for?", ["intracardiac", "intercostal", "intravenous"], "c"),
    ("What does 'JCAHO' stand for?", ["The Joint Commission on Accreditation of Healthcare Organizations", "The Joint Committee on Health Accreditation Organizations", "The Joint Council on Healthcare Accreditation"], "a"),
    ("What does 'JAMA' stand for?", ["Journal of the American Medical Association", "Journal of the American Mental Association", "Journal of the American Medical Affiliates"], "a"),
    ("What does 'JRA' stand for?", ["juvenile rheumatoid arthritis", "juvenile respiratory ailment", "juvenile renal abnormality"], "a"),
    ("What does 'jt.' stand for?", ["joint", "jugular tube", "joint therapy"], "a"),
    ("What does 'K' stand for?", ["ketones", "kilograms", "potassium"], "c"),
    ("What does 'Kcal' stand for?", ["kilocalories", "kilograms per calorie", "kinetic calories"], "a"),
    ("What does 'kg' stand for?", ["kilogram", "kiloliter", "kilomole"], "a"),
    ("What does 'L' stand for?", ["left", "liter", "leg"], "a"),
    ("What does 'L.' mean?", ["length", "liter", "ligament"], "b"),
    ("What does 'L5' stand for?", ["5th lumbar vertebra", "5th lumbar ligament", "5th lumbar muscle"], "a"),
    ("What does 'lat.' mean?", ["lateral", "latissimus", "larynx"], "a"),
    ("What does 'LE' stand for?", ["lower extremity", "left extremity", "lateral extremity"], "a"),
    ("What does 'LLE' stand for?", ["left lower extremity", "lower left extremity", "left leg extremity"], "a"),
    ("What does 'LUE' stand for?", ["left upper extremity", "left upper eyelid", "left upper ear"], "a"),
    ("What does 'LOP' stand for?", ["loss of position", "lateral oblique position", "length of procedure"], "a"),
    ("What does 'LT' stand for?", ["long-term", "left treatment", "light therapy"], "a"),
    ("What does 'LTG' stand for?", ["long-term goal", "long-term gain", "lateral thoracic girdle"], "a"),
    ("What does 'LUE' stand for?", ["lower urinary excretion", "left upper extremity", "left ulnar extension"], "b"),
    ("What does 'LLE' stand for?", ["left lower extremity", "left lumbar extension", "lower limb examination"], "a"),
    ("What does 'M' stand for?", ["molar", "muscle", "male"], "c"),
    ("What does 'NAD' stand for?", ["no active disease", "nasal administration", "non-acute distress"], "a"),
    ("What does 'NIDDM' stand for?", ["non-insulin dependent diabetes mellitus", "neonatal intensive diabetes management", "nervous immunodeficiency disorder management"], "a"),
    ("What does 'NKDA' stand for?", ["no known drug allergies", "no known dietary allergies", "no known disability assessment"], "a"),
    ("What does 'NPO' stand for?", ["nothing per oral", "no patient operation", "non-patient observation"], "a"),
    ("What does 'O2' stand for?", ["oxygen", "ocean water", "oral exam"], "a"),
    ("What does 'OOB' stand for?", ["out of bed", "out of bounds", "out of balance"], "a"),
    ("What does 'OP' stand for?", ["oral presentation", "outpatient", "osteopathic physician"], "b"),
    ("What does 'OR' stand for?", ["operating room", "oral rehydration", "orthopedic rehabilitation"], "a"),
    ("What does 'P' stand for?", ["pain", "pulse", "prognosis"], "b"),
    ("What does 'p.o.' stand for?", ["per oral", "post operation", "physical order"], "a"),
    ("What does 'PERRLA' stand for?", ["pupils equal, round, reactive to light and accommodation", "post-exercise respiratory rate, light activity", "pulmonary evaluation, right and left anterior"], "a"),
    ("What does 'PMH' stand for?", ["previous mental health", "past medical history", "physical mental health"], "b"),
    ("What does 'prn' stand for?", ["as needed", "post rehydration nutrition", "physical reconditioning"], "a"),
    ("What does 'PT' stand for?", ["physical therapy", "patient treatment", "physical training"], "a"),
    ("What does 'PTA' stand for?", ["physical therapy assistant", "patient treatment area", "physical training assessment"], "a"),
    ("What does 'R' stand for?", ["respiration", "recovery", "restoration"], "a"),
    ("What does 'RA' stand for?", ["rheumatoid arthritis", "respiratory analysis", "renal artery"], "a"),
    ("What does 'ROM' stand for?", ["range of motion", "renal osteopathy", "respiratory output measurement"], "a"),
    ("What does 'S' stand for?", ["saturation", "supervision", "symptom"], "b"),
    ("What does 'SOB' stand for?", ["shortness of breath", "saturation of blood", "sound of breath"], "a"),
    ("What does 'STAT' stand for?", ["statistical", "immediately", "systematic treatment"], "b"),
    ("What does 'TID' stand for?", ["three times a day", "twice in a day", "thrice in a day"], "a"),
    ("What does 'TPR' stand for?", ["temperature, pulse, respiration", "temperature, pressure, respiration", "total patient response"], "a"),
    ("What does 'URI' stand for?", ["upper respiratory infection", "urinary retention inspection", "ultra-radial imaging"], "a"),
    ("What does 'UTI' stand for?", ["urinary tract infection", "upper thoracic inflammation", "urinary temperature index"], "a"),
    ("What does 'WBC' stand for?", ["white blood cells", "whole blood count", "weighted body condition"], "a"),
    ("What does 'WNL' stand for?", ["within normal limits", "whole normal levels", "weighted normal limits"], "a"),
    ("What does 'y/o' stand for?", ["yearly occurrence", "years old", "young onset"], "b")
]


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def run_quiz(questions):
    random.shuffle(questions)
    score = 0
    total_questions = len(questions)

    for i, (question, options, correct_answer) in enumerate(questions, 1):
        clear_console()
        print(f"Question {i}/{total_questions}")
        print(question)
        for idx, option in enumerate(options, start=97):  # 97 is the ASCII for 'a'
            print(f"{chr(idx)}) {option}")

        user_answer = input("Your answer (a/b/c, s to skip, q to quit): ").strip().lower()
        while user_answer not in ['a', 'b', 'c', 's', 'q']:
            user_answer = input("Invalid input. Please enter a, b, c, s to skip, or q to quit: ").strip().lower()

        if user_answer == 'q':
            print("\nQuiz terminated by user.")
            break
        elif user_answer == 's':
            continue
        elif user_answer == correct_answer:
            print("\nCorrect, you hot b!tch!")
            score += 1
        else:
            correct_index = ord(correct_answer) - 97  # Convert 'a', 'b', 'c' to 0, 1, 2
            print(f"\nIncorrect, the correct answer was {correct_answer}) {options[correct_index]}")

        input("Press Enter to continue...")

    clear_console()
    print(f"\nYour final score is {score}/{total_questions}")
    print(f"\nPercentage: {score/total_questions*100:.2f}%")

if __name__ == "__main__":
    run_quiz(questions)
