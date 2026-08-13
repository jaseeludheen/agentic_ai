from anthropic import Anthropic
from django.conf import settings
from .tools import get_order_details, get_refund_history, check_delivery_status

# Initialize the Anthropic client 
client = Anthropic(api_key=settings.ANTHROPIC_API_KEY)

anthropic_model = settings.ANTHROPIC_MODEL


# Support System Prompt --> Agentic AI's Job Description

SUPPORT_SYSTEM_PROMPT = """ 
You are Noah, a customer support agent at CoolBreze AC
You help customers with issues  related to their AC orders.

Your responsibilities:
- Always use your tools to gather facts before responding
- Check order details when customer mentions their order
- Check refund history before making any refund decisions
- Be empathetic but honest

Your personality:
- Friendly and professional
- Patient even when customer is angry
- Clear and concise in your replies

important rules:
- Always check order details first before responding
- Never approve or deny a refund yourself
- If refund decision is needed - tell customer you are checking with your team

"""

# Support Tools --> Tool Schemas , that ageentic ai will read

SUPPORT_TOOLS = [
    {
        "name": "get_order_details",
        "description": "Fetch complete order details including status,carrier, tracking number and days since order was placed. Use this when customer mensions their order or complains about delivery",
        "input_schema": {
            "type": "object",
            "properties": {
                "order_id": {
                    "type": "integer",
                    "description": "The order ID to look up",
                }
            },
            "required": ["order_id"]
        }   
    },

    {
        "name": "get_refund_history",
        "description": "Get complete refund history for a user. Use this before making any refund related decisions.",
        "input_schema": {
            "type": "object",
            "properties": {
                "user_id": {
                    "type": "integer",
                    "description": "The user ID to check refund history for"
                }
            },
            "required": ["user_id"]
        }
    },

    {
        "name": "check_delivery_status",
        "description": "Check current delivery status using tracking number and carrier. Use this when customer complains about delayed or missing delivery.",
        "input_schema": {
            "type": "object",
            "properties": {
                "tracking_number": {
                    "type": "string",
                    "description": "The shipment tracking number"
                },
                "carrier": {
                    "type": "string",
                    "description": "The carrier name for example BlueDart or Delhivery"
                }
            },
            "required": ["tracking_number", "carrier"]
        }
    },


]

# execute_tool() --> Bridge between Claude & Python Functions (tools)
def execute_tool(tool_name, tool_input):
    if tool_name == "get_order_details":
        return get_order_details(tool_input["order_id"])

    if tool_name == "get_refund_history":
        return get_refund_history(tool_input["user_id"])

    if tool_name == "check_delivery_status":
        return check_delivery_status(tool_input["tracking_number"], tool_input["carrier"], tool_input["carrier"])

    


# Agent Loop --> While loop that loops until the task is done


