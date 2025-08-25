# /tools/converter.py
from fpdf import FPDF

class PDFConverter:
    """A tool to convert Markdown text to a PDF file using a Unicode font."""
    
    @staticmethod
    def markdown_to_pdf(markdown_text: str, output_filename: str) -> bool:
        """
        Converts a string of Markdown text into a PDF file.

        Args:
            markdown_text: The string containing Markdown formatted text.
            output_filename: The path to save the output PDF file.

        Returns:
            True if conversion was successful, False otherwise.
        """
        try:
            pdf = FPDF()
            pdf.add_page()
            
            # ADDED: Add the Unicode font
            # The 'uni=True' is important for Unicode support
            pdf.add_font('DejaVu', '', './fonts/DejaVuSans.ttf', uni=True)
            
            # CHANGED: Set the font to our new Unicode font
            pdf.set_font('DejaVu', '', 12)
            
            # Use the multi_cell with markdown=True
            pdf.multi_cell(0, 10, text=markdown_text, markdown=True)
            
            pdf.output(output_filename)
            return True
        except Exception as e:
            print(f"Error converting to PDF: {e}")
            return False