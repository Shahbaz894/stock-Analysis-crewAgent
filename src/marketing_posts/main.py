
# # main.py
# import streamlit as st
# from logger import setup_logger  # Importing the logger setup function

# # Setup logger
# logger = setup_logger("CrewAIApp")

# # Set up Streamlit page configuration
# st.set_page_config(page_title="Marketing Strategy Generator", page_icon="📊", layout="centered")

# # Header for the Streamlit page
# st.title("🎯 Marketing Strategy Generator with CrewAI")

# # Start logging the app startup
# logger.info("CrewAIApp started.")

# def display_success_message(message):
#     """Displays a custom success message in a beautiful, centered way."""
#     st.markdown(f"<h3 style='text-align: center; color: green;'>{message}</h3>", unsafe_allow_html=True)

# def display_error_message(message):
#     """Displays a custom error message in a beautiful, centered way."""
#     st.markdown(f"<h3 style='text-align: center; color: red;'>{message}</h3>", unsafe_allow_html=True)

# def run_crewai(inputs):
#     """Runs the CrewAI workflow with the given inputs and displays results in Streamlit."""
#     try:
#         # Example CrewAI execution (replace with your actual logic)
#         result = "CrewAI Execution Result"  # Placeholder for actual result
#         st.write("## 🎯 CrewAI Execution Results")
#         st.write(result)
#         logger.info(f"CrewAI execution completed successfully for product: {inputs['product_name']}")
#         display_success_message(f"Successfully generated marketing strategy for {inputs['product_name']}")
#         return result
#     except Exception as e:
#         error_message = f"An error occurred during CrewAI execution: {e}"
#         st.error(error_message)
#         logger.error(f"An error occurred during CrewAI execution: {e}", exc_info=True)
#         display_error_message("Oops! Something went wrong. Please try again later.")

# def train_crewai(inputs, n_iterations):
#     """Trains the CrewAI workflow and displays progress in Streamlit."""
#     try:
#         with st.spinner(f"Training CrewAI for {n_iterations} iterations..."):
#             # Replace with your actual training logic
#             result = f"Trained CrewAI for {n_iterations} iterations successfully!"  # Placeholder result
#             st.success("CrewAI training completed successfully!")
#             st.write("## 📈 Training Results")
#             st.write(result)
#             logger.info(f"CrewAI training completed for product: {inputs['product_name']} with {n_iterations} iterations.")
#             display_success_message(f"Successfully trained CrewAI for {inputs['product_name']}")
#             return result
#     except Exception as e:
#         error_message = f"An error occurred during CrewAI training: {e}"
#         st.error(error_message)
#         logger.error(f"An error occurred during CrewAI training: {e}", exc_info=True)
#         display_error_message("Oops! Something went wrong during training. Please try again later.")

# def main():
#     """Main function to run the Streamlit app and provide interactive input to the user."""
#     # User input: Product Name
#     product_name = st.text_input("Enter the Product Name for Marketing Strategy:", "")

#     # if not product_name:
#     #     st.warning("Please enter a product name to continue.")
#     #     return

#     # Define inputs dynamically based on user input
#     inputs = {
#         'product_name': product_name,
#         'customer_domain': 'crewai.com',
#         'project_description': f"""
#         CrewAI, a leader in AI-driven automation, is creating a marketing strategy for **{product_name}**. 
#         The goal is to boost brand awareness, highlight key features, and attract enterprise clients.

#         **Customer Domain:** AI and Automation Solutions  
#         **Project Overview:** Crafting a targeted marketing strategy for {product_name}, including competitor analysis, 
#         potential target audience, and recommended marketing channels.
#         """,
#         'expected_output': f"A detailed marketing strategy plan for {product_name}, including success stories and market positioning.",
#         'description': f"Generate a marketing strategy plan for {product_name} targeting enterprise clients.",
#         'config': {},  # Include necessary configurations
#         'agent': 'MarketingAgent',  # Adjust agent as needed
#     }

#     action = st.radio("Choose an action:", ("Run CrewAI", "Train CrewAI"))

#     if action == "Run CrewAI":
#         if st.button("Execute"):
#             logger.info(f"User triggered CrewAI execution for product: {product_name}")
#             run_crewai(inputs)

#     elif action == "Train CrewAI":
#         n_iterations = st.number_input("Number of iterations", min_value=1, value=10)
#         if st.button("Train"):
#             logger.info(f"User triggered CrewAI training for product: {product_name} with {n_iterations} iterations.")
#             train_crewai(inputs, int(n_iterations))

# if __name__ == "__main__":
#     main()


# main.py
import streamlit as st
from logger import setup_logger  # Importing the logger setup function

# Setup logger
logger = setup_logger("CrewAIApp")

# Set up Streamlit page configuration
st.set_page_config(page_title="Marketing Strategy Generator", page_icon="📊", layout="centered")

# Header for the Streamlit page
st.title("🎯 Marketing Strategy Generator with CrewAI")

# Start logging the app startup
logger.info("CrewAIApp started.")

def display_success_message(message):
    """Displays a custom success message in a beautiful, centered way."""
    st.markdown(f"<h3 style='text-align: center; color: green;'>{message}</h3>", unsafe_allow_html=True)

def display_error_message(message):
    """Displays a custom error message in a beautiful, centered way."""
    st.markdown(f"<h3 style='text-align: center; color: red;'>{message}</h3>", unsafe_allow_html=True)

def run_crewai(inputs):
    """Runs the CrewAI workflow with the given inputs and displays results in Streamlit."""
    try:
        # Example logic to generate a detailed marketing strategy
        result = generate_marketing_strategy(inputs)
        
        # Display the results in a more structured way
        st.write("## 🎯 CrewAI Execution Results")
        
        # Example strategy: You can format the output as per your requirements
        st.write(f"### Marketing Strategy for {inputs['product_name']}")
        st.write(f"**Project Overview:** {inputs['project_description']}")
        st.write(f"**Expected Output:** {inputs['expected_output']}")
        st.write(f"**Strategy Details:**")
        st.write(result)  # Display the actual result generated by CrewAI

        # Log the success
        logger.info(f"CrewAI execution completed successfully for product: {inputs['product_name']}")
        display_success_message(f"Successfully generated marketing strategy for {inputs['product_name']}")
        
        return result
    except Exception as e:
        error_message = f"An error occurred during CrewAI execution: {e}"
        st.error(error_message)
        logger.error(f"An error occurred during CrewAI execution: {e}", exc_info=True)
        display_error_message("Oops! Something went wrong. Please try again later.")

def train_crewai(inputs, n_iterations):
    """Trains the CrewAI workflow and displays progress in Streamlit."""
    try:
        with st.spinner(f"Training CrewAI for {n_iterations} iterations..."):
            # Replace with your actual training logic
            result = f"Trained CrewAI for {n_iterations} iterations successfully!"  # Placeholder result
            st.success("CrewAI training completed successfully!")
            st.write("## 📈 Training Results")
            st.write(result)
            logger.info(f"CrewAI training completed for product: {inputs['product_name']} with {n_iterations} iterations.")
            display_success_message(f"Successfully trained CrewAI for {inputs['product_name']}")
            return result
    except Exception as e:
        error_message = f"An error occurred during CrewAI training: {e}"
        st.error(error_message)
        logger.error(f"An error occurred during CrewAI training: {e}", exc_info=True)
        display_error_message("Oops! Something went wrong during training. Please try again later.")

def generate_marketing_strategy(inputs):
    """Simulate the generation of a marketing strategy based on inputs."""
    # Simulate the strategy generation process (replace this with CrewAI logic)
    strategy = f"""
    **Target Audience:** Tech-savvy decision-makers in medium to large enterprises.
    
    **Key Features of {inputs['product_name']}:**
    - Cutting-edge AI technology
    - Easy integration with existing systems
    - Scalable solutions for various enterprise needs
    
    **Recommended Marketing Channels:**
    - LinkedIn for targeting professionals
    - Webinars to demonstrate product capabilities
    - Content marketing (articles, blogs) to increase brand awareness
    
    **Success Stories:**
    - Success with leading enterprises like XYZ Corp.
    - Case studies demonstrating the transformative power of CrewAI solutions.
    
    **Market Positioning:**
    - Position {inputs['product_name']} as a leader in AI automation.
    - Highlight its ease of use and integration, emphasizing how it saves time and improves efficiency.
    """
    return strategy

def main():
    """Main function to run the Streamlit app and provide interactive input to the user."""
    # User input: Product Name
    product_name = st.text_input("Enter the Product Name for Marketing Strategy:", "")

    # if not product_name:
    #     st.warning("Please enter a product name to continue.")
    #     return

    # Define inputs dynamically based on user input
    inputs = {
        'product_name': product_name,
        'customer_domain': 'crewai.com',
        'project_description': f"""
        CrewAI, a leader in AI-driven automation, is creating a marketing strategy for **{product_name}**. 
        The goal is to boost brand awareness, highlight key features, and attract enterprise clients.

        **Customer Domain:** AI and Automation Solutions  
        **Project Overview:** Crafting a targeted marketing strategy for {product_name}, including competitor analysis, 
        potential target audience, and recommended marketing channels.
        """,
        'expected_output': f"A detailed marketing strategy plan for {product_name}, including success stories and market positioning.",
        'description': f"Generate a marketing strategy plan for {product_name} targeting enterprise clients.",
        'config': {},  # Include necessary configurations
        'agent': 'MarketingAgent',  # Adjust agent as needed
    }

    action = st.radio("Choose an action:", ("Run CrewAI", "Train CrewAI"))

    if action == "Run CrewAI":
        if st.button("Execute"):
            logger.info(f"User triggered CrewAI execution for product: {product_name}")
            run_crewai(inputs)

    elif action == "Train CrewAI":
        n_iterations = st.number_input("Number of iterations", min_value=1, value=10)
        if st.button("Train"):
            logger.info(f"User triggered CrewAI training for product: {product_name} with {n_iterations} iterations.")
            train_crewai(inputs, int(n_iterations))

if __name__ == "__main__":
    main()
