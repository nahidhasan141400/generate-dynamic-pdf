from datetime import datetime
from io import BytesIO
from flask import Flask, request, Response, jsonify
from jsonschema import ValidationError, validate
from src.generate_visa_pdf import get_visa_html, generate_visa_pdf
from src.generate_itenary_pdf import get_itenary_html, generate_itenary_pdf
from src.generate_undertaking_single_pdf import (
    get_undertaking_single_html,
    generate_undertaking_single_pdf,
)
from src.generate_undertaking_family_pdf import (
    get_undertaking_family_html,
    generate_undertaking_family_pdf,
)

from src.generate_authorize_pdf import get_authorize_html, generate_authorize_pdf
from xhtml2pdf import pisa
from src.schema import (
    itenary_schema,
    visa_schema,
    undertaking_single_schema,
    undertaking_family_schema,
    authorize_schema,
)

app = Flask(__name__)


@app.route("/generate/visa/", methods=["POST"])
def generate_visa_pdf_route():
    try:
        data = request.get_json(silent=True)

        if data is None:
            return (
                jsonify(
                    {
                        "message": "Request body is not valid JSON!",
                        "code": "invalid-json",
                    }
                ),
                400,
            )

        validate(data, visa_schema)

        pdf_buffer = BytesIO()

        try:
            content = get_visa_html(
                data.get("name"), data.get("passport"), data.get("purpose"), data.get("guest_country")
            )
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            return (
                jsonify(
                    {
                        "message": f"PDF generation error: {str(e)}",
                        "code": "pdf-gen-error",
                    }
                ),
                500,
            )

        return Response(pdf_buffer, content_type="application/pdf")

    except ValidationError as e:
        return (
            jsonify(
                {
                    "message": "Request doesn't contain valid data!",
                    "error": str(e),
                    "code": "invalid-request",
                }
            ),
            400,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "message": "Internal Server Error",
                    "code": "server-break",
                    "error": str(e),
                }
            ),
            500,
        )


@app.route("/generate/itenary/", methods=["POST"])
def generate_itenary_pdf_route():
    try:
        data = request.get_json(silent=True)

        if data is None:
            return (
                jsonify(
                    {
                        "message": "Request body is not valid JSON!",
                        "code": "invalid-json",
                    }
                ),
                400,
            )

        validate(data, itenary_schema)

        pdf_buffer = BytesIO()

        try:
            content = get_itenary_html(data)
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            return (
                jsonify(
                    {
                        "message": "PDF generation valid",
                        "code": "pdf-gen-error",
                        "error": str(e),
                    }
                ),
                500,
            )

        return Response(pdf_buffer, content_type="application/pdf")

    except ValidationError as e:
        return (
            jsonify(
                {
                    "message": "Request doesn't contain valid data!",
                    "error": str(e),
                    "code": "invalid-request",
                }
            ),
            400,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "message": "Internal Server Error",
                    "code": "server-break",
                    "error": str(e),
                }
            ),
            500,
        )


@app.route("/generate/undertaking/single/", methods=["POST"])
def generate_undertaking_single_pdf_route():
    try:
        data = request.get_json(silent=True)

        if data is None:
            return (
                jsonify(
                    {
                        "message": "Request body is not valid JSON!",
                        "code": "invalid-json",
                    }
                ),
                400,
            )

        validate(data, undertaking_single_schema)

        pdf_buffer = BytesIO()

        try:
            content = get_undertaking_single_html(data.get("name"))
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            return (
                jsonify(
                    {
                        "message": f"PDF generation error: {str(e)}",
                        "code": "pdf-gen-error",
                    }
                ),
                500,
            )

        return Response(pdf_buffer, content_type="application/pdf")

    except ValidationError as e:
        return (
            jsonify(
                {
                    "message": "Request doesn't contain valid data!",
                    "error": str(e),
                    "code": "invalid-request",
                }
            ),
            400,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "message": "Internal Server Error",
                    "code": "server-break",
                    "error": str(e),
                }
            ),
            500,
        )


@app.route("/generate/undertaking/family/", methods=["POST"])
def generate_undertaking_family_pdf_route():
    try:
        data = request.get_json(silent=True)

        if data is None:
            return (
                jsonify(
                    {
                        "message": "Request body is not valid JSON!",
                        "code": "invalid-json",
                    }
                ),
                400,
            )

        validate(data, undertaking_family_schema)

        pdf_buffer = BytesIO()

        try:
            content = get_undertaking_family_html(data.get("name"), data.get("array"))
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            return (
                jsonify(
                    {
                        "message": f"PDF generation error: {str(e)}",
                        "code": "pdf-gen-error",
                    }
                ),
                500,
            )

        return Response(pdf_buffer, content_type="application/pdf")

    except ValidationError as e:
        return (
            jsonify(
                {
                    "message": "Request doesn't contain valid data!",
                    "error": str(e),
                    "code": "invalid-request",
                }
            ),
            400,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "message": "Internal Server Error",
                    "code": "server-break",
                    "error": str(e),
                }
            ),
            500,
        )


@app.route("/generate/authorize/", methods=["POST"])
def generate_authorize_pdf_route():
    try:
        data = request.get_json(silent=True)

        if data is None:
            return (
                jsonify(
                    {
                        "message": "Request body is not valid JSON!",
                        "code": "invalid-json",
                    }
                ),
                400,
            )

        validate(data, authorize_schema)

        pdf_buffer = BytesIO()

        try:
            content = get_authorize_html(data.get("name"))
            pisa.CreatePDF(content, dest=pdf_buffer)
            pdf_buffer.seek(0)

        except Exception as e:
            return (
                jsonify(
                    {
                        "message": f"PDF generation error: {str(e)}",
                        "code": "pdf-gen-error",
                    }
                ),
                500,
            )

        return Response(pdf_buffer, content_type="application/pdf")

    except ValidationError as e:
        return (
            jsonify(
                {
                    "message": "Request doesn't contain valid data!",
                    "error": str(e),
                    "code": "invalid-request",
                }
            ),
            400,
        )

    except Exception as e:
        return (
            jsonify(
                {
                    "message": "Internal Server Error",
                    "code": "server-break",
                    "error": str(e),
                }
            ),
            500,
        )


@app.route("/generate/test/", methods=["GET"])
def test():
    generate_itenary_pdf(
        {
            "guests": [
                {"name": "Al-imam", "passport": 43534},
                {"name": "Al-imam", "passport": 43534},
            ],
            "itenary": [
                {
                    "date": datetime.today().strftime("%Y-%m-%d"),
                    "from": "AirPost",
                    "to": "Hotel valentilo",
                },
                {
                    "date": datetime.today().strftime("%Y-%m-%d"),
                    "from": "AirPost",
                    "to": "Hotel valentilo",
                },
            ],
        },
    )

    generate_visa_pdf("HelloLUEHUIG", "A3485G45", "visiting","NAhid","Nel")

    generate_undertaking_single_pdf("Nirob")
    generate_undertaking_family_pdf(
        "Nirob", [{"sl": "1", "name": "Imam", "number": "23847", "remarks": "self"}]
    )

    generate_authorize_pdf(
        {
            "client": "Nirob",
            "client_passport_number": "D2786G#4",
            "authorizer": "Imam",
            "relationship": "Self",
            "authorizer_passport_number": "1924AD343",
            "contact": "email@mail.com",
            "name_ava": "USA_MILITARY",
            "address_ava": "SOME_WHERE_CLOSE",
        }
    )

    return (
        jsonify({"success": True}),
        201,
    )


if __name__ == "__main__":
    app.run(debug=True)
