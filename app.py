from fastapi import FastAPI, UploadFile, File, Form, HTTPException
import uuid

app = FastAPI()


Candidates = {}


@app.get("/")
def home():
    return {"message": "Mini Resume API Working"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/Candidates")
def add_candidate(
    full_name: str = Form(...),
    dob: str = Form(...),
    contact_number: str = Form(...),
    address: str = Form(...),
    qualification: str = Form(...),
    graduation_year: int = Form(...),
    experience: int = Form(...),
    skills: str = Form(...),
    resume: UploadFile = File(...)
):
    cid = str(uuid.uuid4())

    Candidates[cid] = {
        "id": cid,
        "full_name": full_name,
        "dob": dob,
        "contact_number": contact_number,
        "address": address,
        "qualification": qualification,
        "graduation_year": graduation_year,
        "experience": experience,
        "skills": skills.split(","),
        "resume_file": resume.filename
    }

    return {"message": "Candidate added", "id": cid}


@app.get("/Candidates")
def list_candidates():
    return list(Candidates.values())


@app.get("/Candidates/{cid}")
def get_candidate(cid: str):
    if cid not in Candidates:
        raise HTTPException(status_code=404, detail="Not found")
    return Candidates[cid]


@app.delete("/Candidates/{cid}")
def delete_candidate(cid: str):
    if cid not in Candidates:
        raise HTTPException(status_code=404, detail="Not found")
    del Candidates[cid]
    return {"message": "Deleted"}
