
import streamlit as st
import requests

st.set_page_config(
    page_title="Pakistan Drug Information Center",
    page_icon="💊",
    layout="wide"
)

st.title("💊 Pakistan Drug Information Center")
st.caption("Covering Pakistani & International Medicines")

# Pakistani medicines database
pakistan_medicines = {
    "panadol": {
        "brand": "Panadol",
        "generic": "Paracetamol",
        "dose": "500mg - 1000mg",
        "use": "Fever, headache, pain relief",
        "times": "3-4 times daily",
        "warning": "Do not exceed 4g per day",
        "company": "GSK Pakistan"
    },
    "brufen": {
        "brand": "Brufen",
        "generic": "Ibuprofen",
        "dose": "400mg - 600mg",
        "use": "Pain, inflammation, fever",
        "times": "3 times daily after food",
        "warning": "Avoid if stomach ulcer",
        "company": "Abbott Pakistan"
    },
    "flagyl": {
        "brand": "Flagyl",
        "generic": "Metronidazole",
        "dose": "400mg - 500mg",
        "use": "Bacterial and parasitic infections",
        "times": "3 times daily",
        "warning": "Avoid alcohol during treatment",
        "company": "Sanofi Pakistan"
    },
    "augmentin": {
        "brand": "Augmentin",
        "generic": "Amoxicillin + Clavulanate",
        "dose": "625mg - 1000mg",
        "use": "Bacterial infections",
        "times": "2-3 times daily",
        "warning": "Complete full course!",
        "company": "GSK Pakistan"
    },
    "ponstan": {
        "brand": "Ponstan",
        "generic": "Mefenamic Acid",
        "dose": "250mg - 500mg",
        "use": "Pain, menstrual cramps",
        "times": "3 times daily after food",
        "warning": "Avoid if kidney problems",
        "company": "Pfizer Pakistan"
    },
    "risek": {
        "brand": "Risek",
        "generic": "Omeprazole",
        "dose": "20mg - 40mg",
        "use": "Acidity, stomach ulcer, GERD",
        "times": "Once daily before breakfast",
        "warning": "Long term use needs doctor advice",
        "company": "Searle Pakistan"
    },
    "glucophage": {
        "brand": "Glucophage",
        "generic": "Metformin",
        "dose": "500mg - 1000mg",
        "use": "Type 2 Diabetes",
        "times": "2-3 times daily with food",
        "warning": "Monitor kidney function",
        "company": "Merck Pakistan"
    },
    "amoxil": {
        "brand": "Amoxil",
        "generic": "Amoxicillin",
        "dose": "250mg - 500mg",
        "use": "Bacterial infections",
        "times": "3 times daily",
        "warning": "Complete full antibiotic course!",
        "company": "GSK Pakistan"
    },
    "norvasc": {
        "brand": "Norvasc",
        "generic": "Amlodipine",
        "dose": "5mg - 10mg",
        "use": "High blood pressure, chest pain",
        "times": "Once daily",
        "warning": "Do not stop suddenly",
        "company": "Pfizer Pakistan"
    },
    "cipro": {
        "brand": "Cipro",
        "generic": "Ciprofloxacin",
        "dose": "250mg - 500mg",
        "use": "Bacterial infections, UTI",
        "times": "2 times daily",
        "warning": "Avoid dairy products with this medicine",
        "company": "Bayer Pakistan"
    },
    "zithromax": {
        "brand": "Zithromax",
        "generic": "Azithromycin",
        "dose": "250mg - 500mg",
        "use": "Respiratory infections, pneumonia",
        "times": "Once daily for 3-5 days",
        "warning": "Complete full course",
        "company": "Pfizer Pakistan"
    },
    "voltaren": {
        "brand": "Voltaren",
        "generic": "Diclofenac",
        "dose": "25mg - 50mg",
        "use": "Pain, arthritis, inflammation",
        "times": "2-3 times daily after food",
        "warning": "Avoid if heart or kidney problems",
        "company": "Novartis Pakistan"
    }
}

with st.sidebar:
    st.header("About")
    st.info("Built by Ramsha — Biochemistry Graduate + AI Developer")
    st.success("Pakistani + International medicines!")
    st.warning("Always consult your doctor!")
    
    st.header("Common Pakistani Medicines")
    pak_meds = ["Panadol", "Brufen", "Flagyl", 
                "Augmentin", "Risek", "Glucophage",
                "Amoxil", "Norvasc", "Cipro"]
    
    for med in pak_meds:
        if st.button(med, key=med):
            st.session_state.medicine = med

tab1, tab2 = st.tabs([
    "Search Medicine",
    "Medicine List"
])

with tab1:
    st.header("Search Any Medicine")
    
    medicine_name = st.text_input(
        "Enter medicine name:",
        placeholder="e.g. Panadol, Brufen, Glucophage"
    )
    
    if st.button("Search", type="primary"):
        if medicine_name:
            search_key = medicine_name.lower().strip()
            
            if search_key in pakistan_medicines:
                med = pakistan_medicines[search_key]
                
                st.success(f"Found: {med['brand']}!")
                
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Basic Information")
                    st.write("Brand Name:", med["brand"])
                    st.write("Generic Name:", med["generic"])
                    st.write("Company:", med["company"])
                    st.write("Dose:", med["dose"])
                
                with col2:
                    st.subheader("How to Use")
                    st.info("Use: " + med["use"])
                    st.success("Times: " + med["times"])
                    st.warning("Warning: " + med["warning"])
                
                st.error("Always consult your doctor!")
                
            else:
                st.info(f"Searching FDA database for {medicine_name}...")
                try:
                    response = requests.get(
                        f"https://api.fda.gov/drug/label.json?search={medicine_name}&limit=1",
                        timeout=15
                    )
                    data = response.json()
                    
                    if "results" in data:
                        drug = data["results"][0]
                        openfda = drug.get("openfda", {})
                        
                        st.success(f"Found in FDA database!")
                        
                        col1, col2 = st.columns(2)
                        
                        with col1:
                            st.subheader("Basic Information")
                            if "brand_name" in openfda:
                                st.write("Brand:", openfda["brand_name"][0])
                            if "generic_name" in openfda:
                                st.write("Generic:", openfda["generic_name"][0])
                            if "route" in openfda:
                                st.write("Route:", openfda["route"][0])
                        
                        with col2:
                            st.subheader("Medical Details")
                            if "purpose" in drug:
                                st.info("Purpose: " + drug["purpose"][0][:200])
                            if "warnings" in drug:
                                st.warning("Warning: " + drug["warnings"][0][:200])
                        
                        st.error("Always consult your doctor!")
                    else:
                        st.error("Medicine not found! Try another name.")
                        
                except:
                    st.error("Search failed. Please try again!")
        else:
            st.warning("Please enter medicine name!")

with tab2:
    st.header("All Pakistani Medicines")
    st.write("We have information for these medicines:")
    
    cols = st.columns(3)
    for i, (key, med) in enumerate(pakistan_medicines.items()):
        with cols[i % 3]:
            with st.expander(med["brand"]):
                st.write("Generic:", med["generic"])
                st.write("Use:", med["use"])
                st.write("Dose:", med["dose"])

st.divider()
st.caption("Pakistan Drug Info Center — Built by Ramsha | Biochemistry + AI")
