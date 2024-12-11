
from django.shortcuts import render
from django.http import JsonResponse
import black  # Python formatter
import cssbeautifier  # CSS formatter
import jsbeautifier  # JavaScript formatter
from bs4 import BeautifulSoup# HTML formatter
import subprocess  # For invoking clang-format for C/C++

# formatter/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')




# Function to format Python code
def format_python(code):
    try:
        return black.format_str(code, mode=black.Mode())
    except Exception as e:
        return f"Error formatting Python code: {str(e)}"

# Function to format CSS code
def format_css(code):
    try:
        return cssbeautifier.beautify(code)
    except Exception as e:
        return f"Error formatting CSS code: {str(e)}"

# Function to format JavaScript code
def format_js(code):
    try:
        return jsbeautifier.beautify(code)
    except Exception as e:
        return f"Error formatting JavaScript code: {str(e)}"



# Function to format HTML code
def format_html(code):
    try:
        # Parse the HTML code using BeautifulSoup and the 'lxml' parser
        soup = BeautifulSoup(code, 'lxml')

        # Add the DOCTYPE declaration explicitly if it's missing
        if not code.strip().startswith('<!DOCTYPE'):
            formatted_html = f'<!DOCTYPE html>\n{soup.prettify()}'
        else:
            formatted_html = soup.prettify()

        # Return the formatted HTML
        return formatted_html
    except Exception as e:
        return f"Error formatting HTML code: {str(e)}"




# Function to format C/C++ code using clang-format
def format_c_cpp(code):
    try:
        # Write the code to a temporary file
        with open('temp_code.c', 'w') as file:
            file.write(code)
        
        # Run clang-format to format the C/C++ code
        result = subprocess.run(['clang-format', 'temp_code.c'], capture_output=True, text=True)
        
        # Return the formatted code or error message
        if result.returncode == 0:
            return result.stdout
        else:
            return f"Error formatting C/C++ code: {result.stderr}"
    except Exception as e:
        return f"Error formatting C/C++ code: {str(e)}"

def format_code(request):
    if request.method == 'POST':
        code = request.POST.get('code')
        language = request.POST.get('language')

        # Format based on language
        if language == 'python':
            formatted_code = format_python(code)
        elif language == 'css':
            formatted_code = format_css(code)
        elif language == 'javascript':
            formatted_code = format_js(code)
        elif language == 'html':
            formatted_code = format_html(code)
        elif language == 'c' or language == 'cpp':
            formatted_code = format_c_cpp(code)
        else:
            return JsonResponse({'error': 'Unsupported language'}, status=400)
        
        return JsonResponse({'formatted_code': formatted_code})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)
