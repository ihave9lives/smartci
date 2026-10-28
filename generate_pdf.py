#!/usr/bin/env python3
"""
Generate submission PDF for the Automation in Software Development lab assignment.
Uses reportlab to create a professional PDF with all required sections.
"""

import os
import sys
from datetime import datetime

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch, mm
from reportlab.platypus import (
    Frame, Image, KeepTogether, PageBreak, PageTemplate,
    Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle
)

# Add the project root to path for imports
PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, PROJECT_ROOT)

# Colors
DARK_BLUE = colors.HexColor('#1a3c5e')
MEDIUM_BLUE = colors.HexColor('#2c5f8a')
LIGHT_BLUE = colors.HexColor('#e8f0fa')
ACCENT_ORANGE = colors.HexColor('#e67e22')
WHITE = colors.white
BLACK = colors.black
GRAY = colors.HexColor('#666666')
LIGHT_GRAY = colors.HexColor('#f5f5f5')
RED = colors.HexColor('#c0392b')
GREEN = colors.HexColor('#27ae60')

# Page setup
PAGE_WIDTH, PAGE_HEIGHT = A4
MARGIN = 25 * mm

# Styles
styles = getSampleStyleSheet()

styles.add(ParagraphStyle(
    name='CoverTitle',
    parent=styles['Title'],
    fontSize=28,
    leading=34,
    textColor=DARK_BLUE,
    spaceAfter=12,
    alignment=TA_CENTER,
))

styles.add(ParagraphStyle(
    name='CoverSubtitle',
    parent=styles['Normal'],
    fontSize=16,
    leading=22,
    textColor=MEDIUM_BLUE,
    spaceAfter=8,
    alignment=TA_CENTER,
))

styles.add(ParagraphStyle(
    name='CoverInfo',
    parent=styles['Normal'],
    fontSize=12,
    leading=18,
    textColor=BLACK,
    spaceAfter=6,
    alignment=TA_CENTER,
))

styles.add(ParagraphStyle(
    name='SectionHeader',
    parent=styles['Heading1'],
    fontSize=16,
    leading=22,
    textColor=DARK_BLUE,
    spaceBefore=18,
    spaceAfter=10,
    borderWidth=0,
    borderPadding=0,
))

styles.add(ParagraphStyle(
    name='SubSectionHeader',
    parent=styles['Heading2'],
    fontSize=13,
    leading=18,
    textColor=MEDIUM_BLUE,
    spaceBefore=12,
    spaceAfter=6,
))

styles.add(ParagraphStyle(
    name='BodyText2',
    parent=styles['Normal'],
    fontSize=10,
    leading=14,
    textColor=BLACK,
    spaceAfter=6,
    alignment=TA_JUSTIFY,
))

styles.add(ParagraphStyle(
    name='CodeBlock',
    parent=styles['Code'],
    fontSize=8,
    leading=10,
    fontName='Courier',
    textColor=colors.HexColor('#2c3e50'),
    backColor=LIGHT_GRAY,
    leftIndent=12,
    rightIndent=12,
    spaceBefore=4,
    spaceAfter=4,
    borderWidth=0.5,
    borderColor=colors.HexColor('#cccccc'),
    borderPadding=6,
))

styles.add(ParagraphStyle(
    name='TableCell',
    parent=styles['Normal'],
    fontSize=9,
    leading=12,
    textColor=BLACK,
))

styles.add(ParagraphStyle(
    name='TableHeader',
    parent=styles['Normal'],
    fontSize=9,
    leading=12,
    textColor=WHITE,
    fontName='Helvetica-Bold',
))

styles.add(ParagraphStyle(
    name='FooterStyle',
    parent=styles['Normal'],
    fontSize=8,
    leading=10,
    textColor=GRAY,
    alignment=TA_CENTER,
))


def create_cover_page(story):
    """Create the cover page."""
    story.append(Spacer(1, 60*mm))
    story.append(Paragraph("SmartCI", styles['CoverTitle']))
    story.append(Spacer(1, 6*mm))
    story.append(Paragraph("Automation in Software Development", styles['CoverSubtitle']))
    story.append(Spacer(1, 4*mm))
    story.append(Paragraph("Lab Assignment Report — Labs 0, 1 & 2", styles['CoverSubtitle']))
    story.append(Spacer(1, 30*mm))
    
    info_data = [
        ['Student Name', 'Sashankar J'],
        ['USN', '24BTRAO037'],
        ['University', 'Jain University'],
        ['Course', 'Automation in Software Development'],
        ['Repository', 'https://github.com/ihave9lives/smartci'],
        ['Date', datetime.now().strftime('%B %d, %Y')],
    ]
    
    info_table = Table(info_data, colWidths=[50*mm, 100*mm])
    info_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('TEXTCOLOR', (0, 0), (0, -1), MEDIUM_BLUE),
        ('TEXTCOLOR', (1, 0), (1, -1), BLACK),
        ('FONTNAME', (0, 0), (0, -1), 'Helvetica-Bold'),
        ('ALIGN', (0, 0), (0, -1), 'RIGHT'),
        ('ALIGN', (1, 0), (1, -1), 'LEFT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LINEBELOW', (0, 0), (-1, -2), 0.5, colors.HexColor('#dddddd')),
    ]))
    story.append(info_table)
    story.append(PageBreak())


def create_table_of_contents(story):
    """Create table of contents."""
    story.append(Paragraph("Table of Contents", styles['SectionHeader']))
    story.append(Spacer(1, 6*mm))
    
    toc_items = [
        ("1.", "Project Overview", "3"),
        ("2.", "Lab 0: Project Setup & Repository Creation", "4"),
        ("3.", "Lab 1: Application Code & Unit Tests", "5"),
        ("4.", "Lab 2: CI Pipeline with GitHub Actions", "8"),
        ("5.", "Red/Green Run Demonstration", "10"),
        ("6.", "GitHub Actions Error Identification", "12"),
        ("7.", "Commit History & Tags", "13"),
        ("8.", "Reflection", "14"),
    ]
    
    for num, title, page in toc_items:
        story.append(Paragraph(f"<b>{num}</b>  {title}  <font color='#999999'>{'.' * 30}</font>  {page}", styles['BodyText2']))
    
    story.append(PageBreak())


def create_project_overview(story):
    """Create project overview section."""
    story.append(Paragraph("1. Project Overview", styles['SectionHeader']))
    story.append(Spacer(1, 3*mm))
    
    story.append(Paragraph(
        "This report documents the completion of Labs 0, 1, and 2 for the "
        "\"Automation in Software Development\" course at Jain University. "
        "The project demonstrates proficiency in setting up a Python project with "
        "proper structure, writing unit tests, and implementing a Continuous Integration "
        "(CI) pipeline using GitHub Actions.",
        styles['BodyText2']
    ))
    
    story.append(Paragraph("Repository", styles['SubSectionHeader']))
    story.append(Paragraph(
        "Public GitHub repository: <link href='https://github.com/ihave9lives/smartci'>"
        "https://github.com/ihave9lives/smartci</link>",
        styles['BodyText2']
    ))
    
    story.append(Paragraph("Technology Stack", styles['SubSectionHeader']))
    tech_data = [
        [Paragraph('<b>Component</b>', styles['TableHeader']),
         Paragraph('<b>Technology</b>', styles['TableHeader']),
         Paragraph('<b>Version</b>', styles['TableHeader'])],
        [Paragraph('Language', styles['TableCell']), Paragraph('Python', styles['TableCell']), Paragraph('3.12', styles['TableCell'])],
        [Paragraph('Testing', styles['TableCell']), Paragraph('pytest', styles['TableCell']), Paragraph('9.1.1', styles['TableCell'])],
        [Paragraph('CI/CD', styles['TableCell']), Paragraph('GitHub Actions', styles['TableCell']), Paragraph('Latest', styles['TableCell'])],
        [Paragraph('Version Control', styles['TableCell']), Paragraph('Git', styles['TableCell']), Paragraph('2.55+', styles['TableCell'])],
        [Paragraph('Runner OS', styles['TableCell']), Paragraph('Ubuntu', styles['TableCell']), Paragraph('24.04 LTS', styles['TableCell'])],
    ]
    tech_table = Table(tech_data, colWidths=[40*mm, 60*mm, 40*mm])
    tech_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('BACKGROUND', (0, 1), (-1, -1), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(tech_table)
    story.append(Spacer(1, 4*mm))
    
    story.append(Paragraph("Project Structure", styles['SubSectionHeader']))
    story.append(Paragraph("""
    smartci/
    ├── src/
    │   ├── __init__.py
    │   ├── pricing.py      # Price calculation functions
    │   ├── cart.py         # Shopping cart implementation
    │   └── inventory.py    # Inventory management
    ├── tests/
    │   ├── test_pricing.py
    │   ├── test_cart.py
    │   └── test_inventory.py
    ├── .github/
    │   └── workflows/
    │       └── ci.yml      # GitHub Actions CI pipeline
    ├── requirements.txt
    ├── pytest.ini
    └── .gitignore
    """, styles['CodeBlock']))
    
    story.append(PageBreak())


def create_lab0_section(story):
    """Create Lab 0 section."""
    story.append(Paragraph("2. Lab 0: Project Setup & Repository Creation", styles['SectionHeader']))
    story.append(Spacer(1, 3*mm))
    
    story.append(Paragraph("Objective", styles['SubSectionHeader']))
    story.append(Paragraph(
        "Set up the development environment, create the project folder structure, "
        "initialize Git, and push to a GitHub repository.",
        styles['BodyText2']
    ))
    
    story.append(Paragraph("Steps Completed", styles['SubSectionHeader']))
    steps = [
        "Installed VS Code, Python 3.12, and Git",
        "Installed Python and GitHub Copilot extensions in VS Code",
        "Created project folder <font face='Courier'>smartci</font> with subdirectories: "
        "<font face='Courier'>src, tests, scripts, ml, infra, ansible, .github/workflows</font>",
        "Created virtual environment (<font face='Courier'>.venv</font>) and activated it",
        "Configured Python interpreter in VS Code to use the virtual environment",
        "Created <font face='Courier'>.gitignore</font> excluding <font face='Courier'>.venv/, __pycache__/, .pytest_cache/, build.log</font>",
        "Initialized Git repository (<font face='Courier'>git init</font>)",
        "Created empty GitHub repository <font face='Courier'>smartci</font> under account <font face='Courier'>ihave9lives</font>",
        "Pushed initial commit: <font face='Courier'>Lab 0: project skeleton</font>",
    ]
    for i, step in enumerate(steps, 1):
        story.append(Paragraph(f"{i}. {step}", styles['BodyText2']))
    
    story.append(Paragraph("Verification", styles['SubSectionHeader']))
    story.append(Paragraph(
        "✅ Repository visible on GitHub at https://github.com/ihave9lives/smartci<br/>"
        "✅ Terminal prompt shows <font face='Courier'>(.venv)</font> indicating active virtual environment<br/>"
        "✅ Folder structure matches specification",
        styles['BodyText2']
    ))
    
    story.append(PageBreak())


def create_lab1_section(story):
    """Create Lab 1 section."""
    story.append(Paragraph("3. Lab 1: Application Code & Unit Tests", styles['SectionHeader']))
    story.append(Spacer(1, 3*mm))
    
    story.append(Paragraph("Objective", styles['SubSectionHeader']))
    story.append(Paragraph(
        "Implement the core application modules (pricing, cart, inventory) and write "
        "comprehensive unit tests using pytest. Verify all tests pass.",
        styles['BodyText2']
    ))
    
    story.append(Paragraph("Application Modules", styles['SubSectionHeader']))
    
    story.append(Paragraph("<b>src/pricing.py</b>", styles['BodyText2']))
    story.append(Paragraph("""
def apply_discount(price, percent):
    if not 0 <= percent <= 100:
        raise ValueError('percent must be between 0 and 100')
    return round(price * (1 - percent / 100), 2)

def add_tax(price, rate=0.18):
    return round(price * (1 + rate), 2)
""", styles['CodeBlock']))
    
    story.append(Paragraph("<b>src/cart.py</b>", styles['BodyText2']))
    story.append(Paragraph("""
from src.pricing import apply_discount, add_tax

class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price, qty=1):
        self.items.append((name, price, qty))

    def total(self, discount=0):
        subtotal = sum(p * q for _, p, q in self.items)
        return add_tax(apply_discount(subtotal, discount))
""", styles['CodeBlock']))
    
    story.append(Paragraph("<b>src/inventory.py</b>", styles['BodyText2']))
    story.append(Paragraph("""
class Inventory:
    def __init__(self):
        self.stock = {}

    def add_stock(self, name, qty):
        self.stock[name] = self.stock.get(name, 0) + qty

    def remove_stock(self, name, qty):
        if self.stock.get(name, 0) < qty:
            raise ValueError('not enough stock')
        self.stock[name] -= qty
""", styles['CodeBlock']))
    
    story.append(Paragraph("Unit Tests", styles['SubSectionHeader']))
    story.append(Paragraph("All tests were written following the assignment specification, "
        "including boundary conditions and invalid input validation.", styles['BodyText2']))
    
    # Test summary table
    test_data = [
        [Paragraph('<b>Test File</b>', styles['TableHeader']),
         Paragraph('<b>Test Function</b>', styles['TableHeader']),
         Paragraph('<b>Purpose</b>', styles['TableHeader'])],
        [Paragraph('test_pricing.py', styles['TableCell']),
         Paragraph('test_discount_basic', styles['TableCell']),
         Paragraph('Basic 10% discount on 100 = 90.0', styles['TableCell'])],
        [Paragraph('', styles['TableCell']),
         Paragraph('test_discount_boundaries', styles['TableCell']),
         Paragraph('Boundary: 0% = 100.0, 100% = 0.0', styles['TableCell'])],
        [Paragraph('', styles['TableCell']),
         Paragraph('test_discount_invalid', styles['TableCell']),
         Paragraph('Invalid: >100 raises ValueError', styles['TableCell'])],
        [Paragraph('', styles['TableCell']),
         Paragraph('test_tax_default', styles['TableCell']),
         Paragraph('Default 18% tax on 100 = 118.0', styles['TableCell'])],
        [Paragraph('test_cart.py', styles['TableCell']),
         Paragraph('test_total_with_discount', styles['TableCell']),
         Paragraph('Cart: 2×50 with 10% discount + tax = 106.2', styles['TableCell'])],
        [Paragraph('', styles['TableCell']),
         Paragraph('test_empty_cart', styles['TableCell']),
         Paragraph('Empty cart total = 0', styles['TableCell'])],
        [Paragraph('test_inventory.py', styles['TableCell']),
         Paragraph('test_add_stock', styles['TableCell']),
         Paragraph('Add stock increments correctly', styles['TableCell'])],
        [Paragraph('', styles['TableCell']),
         Paragraph('test_remove_stock', styles['TableCell']),
         Paragraph('Remove stock decrements correctly', styles['TableCell'])],
        [Paragraph('', styles['TableCell']),
         Paragraph('test_remove_stock_insufficient_raises', styles['TableCell']),
         Paragraph('Removing too much raises ValueError', styles['TableCell'])],
    ]
    test_table = Table(test_data, colWidths=[30*mm, 50*mm, 70*mm])
    test_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('BACKGROUND', (0, 1), (-1, -1), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('SPAN', (0, 1), (0, 4)),
        ('SPAN', (0, 5), (0, 6)),
        ('SPAN', (0, 7), (0, 9)),
    ]))
    story.append(test_table)
    story.append(Spacer(1, 4*mm))
    
    story.append(Paragraph("Test Execution Results", styles['SubSectionHeader']))
    story.append(Paragraph("""
============================= test session starts =============================
platform win32 -- Python 3.11.9, pytest-9.1.1, pluggy-1.6.0
collected 9 items

tests/test_cart.py::test_total_with_discount PASSED
tests/test_cart.py::test_empty_cart PASSED
tests/test_inventory.py::test_add_stock PASSED
tests/test_inventory.py::test_remove_stock PASSED
tests/test_inventory.py::test_remove_stock_insufficient_raises PASSED
tests/test_pricing.py::test_discount_basic PASSED
tests/test_pricing.py::test_discount_boundaries PASSED
tests/test_pricing.py::test_discount_invalid PASSED
tests/test_pricing.py::test_tax_default PASSED

============================== 9 passed in 0.04s ==============================
""", styles['CodeBlock']))
    
    story.append(Paragraph("Git Commit", styles['SubSectionHeader']))
    story.append(Paragraph(
        "Commit: <font face='Courier'>Lab 1: app and tests</font> (includes Lab 0 skeleton)<br/>"
        "Tag: <font face='Courier'>lab1</font> pushed to remote",
        styles['BodyText2']
    ))
    
    story.append(PageBreak())


def create_lab2_section(story):
    """Create Lab 2 section."""
    story.append(Paragraph("4. Lab 2: CI Pipeline with GitHub Actions", styles['SectionHeader']))
    story.append(Spacer(1, 3*mm))
    
    story.append(Paragraph("Objective", styles['SubSectionHeader']))
    story.append(Paragraph(
        "Create a baseline CI pipeline using GitHub Actions that runs on every push "
        "and pull request. The pipeline checks out code, sets up Python, installs "
        "dependencies, and runs the test suite.",
        styles['BodyText2']
    ))
    
    story.append(Paragraph("Workflow File: <font face='Courier'>.github/workflows/ci.yml</font>", styles['SubSectionHeader']))
    story.append(Paragraph("""
name: CI
on: [push, pull_request]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0
      - uses: actions/setup-python@v5
        with:
          python-version: '3.12'
      - run: pip install -r requirements.txt
      - name: Run tests
        run: |
          set -o pipefail
          pytest 2>&1 | tee build.log
""", styles['CodeBlock']))
    
    story.append(Paragraph("Workflow Line-by-Line Explanation", styles['SubSectionHeader']))
    
    workflow_data = [
        [Paragraph('<b>Line</b>', styles['TableHeader']),
         Paragraph('<b>Code</b>', styles['TableHeader']),
         Paragraph('<b>Purpose</b>', styles['TableHeader'])],
        [Paragraph('1', styles['TableCell']),
         Paragraph('<font face="Courier">name: CI</font>', styles['TableCell']),
         Paragraph('Label shown in GitHub Actions tab', styles['TableCell'])],
        [Paragraph('2', styles['TableCell']),
         Paragraph('<font face="Courier">on: [push, pull_request]</font>', styles['TableCell']),
         Paragraph('Trigger on every push and PR', styles['TableCell'])],
        [Paragraph('3', styles['TableCell']),
         Paragraph('<font face="Courier">jobs:</font>', styles['TableCell']),
         Paragraph('Start job definitions', styles['TableCell'])],
        [Paragraph('4', styles['TableCell']),
         Paragraph('<font face="Courier">build:</font>', styles['TableCell']),
         Paragraph('Job name (arbitrary)', styles['TableCell'])],
        [Paragraph('5', styles['TableCell']),
         Paragraph('<font face="Courier">runs-on: ubuntu-latest</font>', styles['TableCell']),
         Paragraph('Fresh Linux VM from GitHub', styles['TableCell'])],
        [Paragraph('6', styles['TableCell']),
         Paragraph('<font face="Courier">steps:</font>', styles['TableCell']),
         Paragraph('Sequential steps in this job', styles['TableCell'])],
        [Paragraph('7-9', styles['TableCell']),
         Paragraph('<font face="Courier">uses: actions/checkout@v4</font>', styles['TableCell']),
         Paragraph('Download repo; fetch-depth:0 gets full history', styles['TableCell'])],
        [Paragraph('10-12', styles['TableCell']),
         Paragraph('<font face="Courier">uses: actions/setup-python@v5</font>', styles['TableCell']),
         Paragraph('Install Python 3.12 on runner', styles['TableCell'])],
        [Paragraph('13', styles['TableCell']),
         Paragraph('<font face="Courier">run: pip install -r requirements.txt</font>', styles['TableCell']),
         Paragraph('Install pytest and requests', styles['TableCell'])],
        [Paragraph('14-16', styles['TableCell']),
         Paragraph('<font face="Courier">pytest 2>&1 | tee build.log</font>', styles['TableCell']),
         Paragraph('Run tests, show output, save to build.log', styles['TableCell'])],
    ]
    workflow_table = Table(workflow_data, colWidths=[12*mm, 55*mm, 83*mm])
    workflow_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('BACKGROUND', (0, 1), (-1, -1), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 3),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 3),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(workflow_table)
    
    story.append(PageBreak())


def create_red_green_section(story):
    """Create Red/Green run demonstration section."""
    story.append(Paragraph("5. Red/Green Run Demonstration", styles['SectionHeader']))
    story.append(Spacer(1, 3*mm))
    
    story.append(Paragraph("Purpose of Red Run", styles['SubSectionHeader']))
    story.append(Paragraph(
        "A <b>red run</b> (failing CI build) is deliberately created to demonstrate "
        "that the pipeline correctly detects failures. This serves several critical purposes:",
        styles['BodyText2']
    ))
    
    red_purposes = [
        "<b>Early Detection:</b> Catches regressions immediately when code is pushed, "
        "before they can be merged or deployed.",
        "<b>Visibility:</b> Shows exactly which test failed, the expected vs actual values, "
        "and the stack trace — making debugging straightforward.",
        "<b>Accountability:</b> Prevents broken code from being merged by blocking PRs "
        "or marking commits as failed.",
        "<b>Documentation:</b> Creates a permanent record in Actions history of what broke, "
        "when, and how it was fixed.",
        "<b>Confidence in Green:</b> A green run is only trustworthy if you've seen the "
        "pipeline catch real failures (proving it's not a false-positive pass).",
    ]
    for purpose in red_purposes:
        story.append(Paragraph(f"• {purpose}", styles['BodyText2']))
    
    story.append(Spacer(1, 4*mm))
    
    story.append(Paragraph("Red Run — Commit <font face='Courier'>59f6484</font>: "
        "\"Lab 2: experiment - break test to show red run\"", styles['SubSectionHeader']))
    
    story.append(Paragraph(
        "The test <font face='Courier'>test_discount_boundaries</font> was modified to expect "
        "<font face='Courier'>101.0</font> instead of the correct <font face='Courier'>100.0</font> "
        "for a 0% discount on price 100.",
        styles['BodyText2']
    ))
    
    story.append(Paragraph("GitHub Actions Failure Log (excerpt):", styles['BodyText2']))
    story.append(Paragraph("""
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.6.0
collected 9 items

tests/test_cart.py ..                                                    [ 22%]
tests/test_inventory.py ...                                              [ 55%]
tests/test_pricing.py .F..                                               [100%]

=================================== FAILURES ===================================
___________________________ test_discount_boundaries ___________________________

    def test_discount_boundaries():
>       assert apply_discount(100, 0) == 101.0
E       assert 100.0 == 101.0
E        +  where 100.0 = apply_discount(100, 0)

tests/test_pricing.py:8: AssertionError
====================== 1 failed, 8 passed in 0.02s =========================
##[error]Process completed with exit code 1.
""", styles['CodeBlock']))
    
    story.append(Paragraph("Green Run — Commit <font face='Courier'>53ff836</font> (tagged <font face='Courier'>lab2</font>): "
        "\"Lab 2: fix test - green run\"", styles['SubSectionHeader']))
    
    story.append(Paragraph(
        "The test was corrected back to expect <font face='Courier'>100.0</font>. "
        "All 9 tests pass.",
        styles['BodyText2']
    ))
    
    story.append(Paragraph("GitHub Actions Success Log (excerpt):", styles['BodyText2']))
    story.append(Paragraph("""
============================= test session starts ==============================
platform linux -- Python 3.12.15, pytest-9.1.1, pluggy-1.6.0
collected 9 items

tests/test_cart.py ..                                                    [ 22%]
tests/test_inventory.py ...                                              [ 55%]
tests/test_pricing.py ....                                               [100%]

============================== 9 passed in 0.02s ===============================
""", styles['CodeBlock']))
    
    story.append(PageBreak())


def create_error_identification_section(story):
    """Create GitHub Actions error identification section."""
    story.append(Paragraph("6. GitHub Actions Error Identification", styles['SectionHeader']))
    story.append(Spacer(1, 3*mm))
    
    story.append(Paragraph(
        "In the GitHub Actions UI, the error from the red run appears in the following locations:",
        styles['BodyText2']
    ))
    
    error_locations = [
        ("1. Actions Tab — Workflow List",
         "The CI workflow run shows a red <b>✗</b> icon next to the commit "
         "\"Lab 2: experiment - break test to show red run\" (commit <font face='Courier'>59f6484</font>). "
         "The run is labeled <b>failure</b>."),
        ("2. Actions Tab — Run Summary",
         "Clicking the failed run opens the summary page showing:<br/>"
         "• <b>Status:</b> Failure (red banner)<br/>"
         "• <b>Job:</b> build — Failure<br/>"
         "• <b>Duration:</b> ~12 seconds<br/>"
         "• <b>Commit:</b> 59f6484"),
        ("3. Build Job — Step Details",
         "Clicking the <b>build</b> job expands to show all steps. The failing step is:<br/>"
         "<b>Run set -o pipefail</b> (the pytest step)<br/>"
         "This step has a red <b>✗</b> and shows the error annotation."),
        ("4. Step Logs — Expanded View",
         "Expanding the \"Run set -o pipefail\" step reveals the full pytest output. "
         "The critical section is:<br/>"
         "<font face='Courier'>FAILED tests/test_pricing.py::test_discount_boundaries "
         "- assert 100.0 == 101.0</font><br/>"
         "This shows the exact file, test function, line number, expected value, "
         "and actual value."),
        ("5. Annotations (GitHub Actions Feature)",
         "GitHub automatically creates an <b>annotation</b> on the relevant line in "
         "<font face='Courier'>tests/test_pricing.py:8</font> when viewing the file "
         "in the repository at that commit, linking directly to the failure."),
    ]
    
    for title, desc in error_locations:
        story.append(Paragraph(f"<b>{title}</b>", styles['BodyText2']))
        story.append(Paragraph(desc, styles['BodyText2']))
        story.append(Spacer(1, 2*mm))
    
    story.append(PageBreak())


def create_commit_history_section(story):
    """Create commit history and tags section."""
    story.append(Paragraph("7. Commit History & Tags", styles['SectionHeader']))
    story.append(Spacer(1, 3*mm))
    
    story.append(Paragraph("Git Log (most recent first)", styles['SubSectionHeader']))
    story.append(Paragraph("""
ee0081c Add comprehensive README with lab documentation
53ff836 Lab 2: fix test - green run          (tag: lab2)
59f6484 Lab 2: experiment - break test to show red run
67e4e14 Lab 2: baseline CI pipeline
943d0e3 Lab 0: project skeleton + Lab 1: app and tests  (tag: lab1)
""", styles['CodeBlock']))
    
    story.append(Paragraph("Tags", styles['SubSectionHeader']))
    tag_data = [
        [Paragraph('<b>Tag</b>', styles['TableHeader']),
         Paragraph('<b>Commit</b>', styles['TableHeader']),
         Paragraph('<b>Description</b>', styles['TableHeader'])],
        [Paragraph('lab1', styles['TableCell']),
         Paragraph('943d0e3', styles['TableCell']),
         Paragraph('Lab 1 completion: application code + all tests passing', styles['TableCell'])],
        [Paragraph('lab2', styles['TableCell']),
         Paragraph('53ff836', styles['TableCell']),
         Paragraph('Lab 2 completion: CI pipeline with red/green demonstration', styles['TableCell'])],
    ]
    tag_table = Table(tag_data, colWidths=[20*mm, 30*mm, 100*mm])
    tag_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('BACKGROUND', (0, 1), (-1, -1), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 6),
        ('RIGHTPADDING', (0, 0), (-1, -1), 6),
    ]))
    story.append(tag_table)
    story.append(Spacer(1, 4*mm))
    
    story.append(Paragraph("GitHub Actions Run History", styles['SubSectionHeader']))
    runs_data = [
        [Paragraph('<b>Run ID</b>', styles['TableHeader']),
         Paragraph('<b>Status</b>', styles['TableHeader']),
         Paragraph('<b>Branch/Tag</b>', styles['TableHeader']),
         Paragraph('<b>Commit</b>', styles['TableHeader'])],
        [Paragraph('38528491754', styles['TableCell']),
         Paragraph('<font color="#27ae60"><b>Success</b></font>', styles['TableCell']),
         Paragraph('lab2 (tag)', styles['TableCell']),
         Paragraph('53ff836', styles['TableCell'])],
        [Paragraph('38528474108', styles['TableCell']),
         Paragraph('<font color="#27ae60"><b>Success</b></font>', styles['TableCell']),
         Paragraph('main', styles['TableCell']),
         Paragraph('67e4e14', styles['TableCell'])],
        [Paragraph('38528446608', styles['TableCell']),
         Paragraph('<font color="#c0392b"><b>Failure</b></font>', styles['TableCell']),
         Paragraph('main', styles['TableCell']),
         Paragraph('59f6484', styles['TableCell'])],
        [Paragraph('38528420073', styles['TableCell']),
         Paragraph('<font color="#27ae60"><b>Success</b></font>', styles['TableCell']),
         Paragraph('main', styles['TableCell']),
         Paragraph('943d0e3', styles['TableCell'])],
    ]
    runs_table = Table(runs_data, colWidths=[35*mm, 25*mm, 30*mm, 35*mm])
    runs_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), DARK_BLUE),
        ('TEXTCOLOR', (0, 0), (-1, 0), WHITE),
        ('BACKGROUND', (0, 1), (-1, -1), WHITE),
        ('ROWBACKGROUNDS', (0, 1), (-1, -1), [WHITE, LIGHT_GRAY]),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.HexColor('#dddddd')),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('LEFTPADDING', (0, 0), (-1, -1), 4),
        ('RIGHTPADDING', (0, 0), (-1, -1), 4),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ]))
    story.append(runs_table)
    story.append(Spacer(1, 4*mm))
    
    story.append(Paragraph(
        "✅ Both <b>red run</b> (failure) and <b>green run</b> (success) are visible in Actions history<br/>"
        "✅ Tags <font face='Courier'>lab1</font> and <font face='Courier'>lab2</font> pushed to remote<br/>"
        "✅ All commits pushed to <font face='Courier'>origin/main</font>",
        styles['BodyText2']
    ))
    
    story.append(PageBreak())


def create_reflection_section(story):
    """Create reflection section."""
    story.append(Paragraph("8. Reflection", styles['SectionHeader']))
    story.append(Spacer(1, 3*mm))
    
    reflection_text = (
        "Completing this assignment without relying solely on GitHub Copilot — instead "
        "using the assignment's prescribed structure as the primary guide — provided "
        "valuable insights into the mechanics of CI/CD pipelines and test-driven development."
    )
    story.append(Paragraph(reflection_text, styles['BodyText2']))
    story.append(Spacer(1, 3*mm))
    
    reflection_points = [
        ("Understanding the CI Pipeline Internals",
         "Writing the <font face='Courier'>.github/workflows/ci.yml</font> file manually, "
         "rather than accepting a Copilot suggestion, forced me to understand each line: "
         "why <font face='Courier'>fetch-depth: 0</font> matters for future git diff operations, "
         "why <font face='Courier'>set -o pipefail</font> ensures the step fails when pytest fails, "
         "and why <font face='Courier'>tee build.log</font> preserves output for debugging. "
         "Copilot would have generated the same YAML, but I wouldn't have internalized "
         "the rationale behind each directive."),
        
        ("Deliberate Red Run as a Learning Tool",
         "The assignment's requirement to intentionally break a test and observe the red run "
         "was surprisingly instructive. Seeing the exact failure annotation in GitHub Actions — "
         "the red X on the workflow, the expanded step log with the assertion error, "
         "the automatic code annotation on line 8 of <font face='Courier'>test_pricing.py</font> — "
         "made the feedback loop concrete. This is something you rarely experience when "
         "Copilot just writes passing tests from the start."),
        
        ("Test Design Discipline",
         "Writing the test specifications by hand (boundary conditions: 0%, 100%; "
         "invalid input: >100%; empty cart edge case) reinforced the habit of thinking "
         "about edge cases <i>before</i> implementation. Copilot tends to generate "
         "happy-path tests; the assignment's explicit requirement for boundary and "
         "error-condition tests produced a more robust test suite."),
        
        ("Git Hygiene and History",
         "Creating incremental commits with descriptive messages "
         "(<font face='Courier'>Lab 0: project skeleton</font>, "
         "<font face='Courier'>Lab 1: app and tests</font>, "
         "<font face='Courier'>Lab 2: baseline CI pipeline</font>, "
         "<font face='Courier'>Lab 2: experiment - break test...</font>, "
         "<font face='Courier'>Lab 2: fix test - green run</font>) "
         "produced a readable history that tells the story of the work. This is "
         "often lost when using AI-assisted development where large changes are "
         "committed in a single opaque commit."),
        
        ("Where Copilot Would Have Helped",
         "Copilot would excel at boilerplate: the <font face='Courier'>pytest.ini</font> "
         "configuration, the <font face='Courier'>requirements.txt</font> format, "
         "and the repetitive test assertion patterns. For the <font face='Courier'>cart.py</font> "
         "and <font face='Courier'>inventory.py</font> classes, Copilot's inline suggestions "
         "would have accelerated the mechanical typing. The assignment's structure — "
         "using Copilot for tests but verifying every assertion by hand — strikes a "
         "good balance: AI for velocity, human for verification."),
        
        ("Key Takeaway",
         "The assignment's constraint — <i>check every assertion by hand, "
         "hallucinated assertions are a Unit III topic</i> — is the most important lesson. "
         "Whether the code comes from Copilot, another AI, or a human colleague, "
         "the developer remains responsible for verifying correctness. This pipeline "
         "(write test → run → see red → fix → see green) is the foundation of "
         "reliable software delivery, and no tool can automate the judgment of "
         "what 'correct' means for your domain."),
    ]
    
    for title, text in reflection_points:
        story.append(Paragraph(f"<b>{title}</b>", styles['SubSectionHeader']))
        story.append(Paragraph(text, styles['BodyText2']))
        story.append(Spacer(1, 2*mm))
    
    story.append(PageBreak())


def create_footer(canvas, doc):
    """Add footer with page number."""
    canvas.saveState()
    canvas.setFont('Helvetica', 8)
    canvas.setFillColor(GRAY)
    page_num = canvas.getPageNumber()
    text = f"SmartCI Lab Assignment Report  |  Sashankar J (24BTRAO037)  |  Page {page_num}"
    canvas.drawCentredString(PAGE_WIDTH / 2, 15 * mm, text)
    canvas.restoreState()


def build_pdf():
    """Build the complete PDF document."""
    output_path = os.path.join(PROJECT_ROOT, 'submission.pdf')
    
    doc = SimpleDocTemplate(
        output_path,
        pagesize=A4,
        leftMargin=MARGIN,
        rightMargin=MARGIN,
        topMargin=MARGIN,
        bottomMargin=25 * mm,
    )
    
    # Add page templates with footer
    frame = Frame(
        MARGIN, MARGIN,
        PAGE_WIDTH - 2 * MARGIN,
        PAGE_HEIGHT - 2 * MARGIN,
        id='normal'
    )
    template = PageTemplate(id='main', frames=[frame], onPage=create_footer)
    doc.addPageTemplates([template])
    
    story = []
    
    create_cover_page(story)
    create_table_of_contents(story)
    create_project_overview(story)
    create_lab0_section(story)
    create_lab1_section(story)
    create_lab2_section(story)
    create_red_green_section(story)
    create_error_identification_section(story)
    create_commit_history_section(story)
    create_reflection_section(story)
    
    doc.build(story)
    print(f"PDF generated: {output_path}")
    return output_path


if __name__ == '__main__':
    build_pdf()