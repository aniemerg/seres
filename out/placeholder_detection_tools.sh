#!/bin/bash
# Placeholder Detection Tools

echo "==================================================================="
echo "PLACEHOLDER DETECTION TOOLS"
echo "==================================================================="

echo ""
echo "1. Stock_material recipes (HIGH PRIORITY):"
echo "-------------------------------------------------------------------"
grep -r "item_id: stock_material" kb/recipes --include="*.yaml" -l | wc -l | xargs echo "Count:"
grep -r "item_id: stock_material" kb/recipes --include="*.yaml" -l

echo ""
echo "2. Placeholder processes (files with 'placeholder' in name):"
echo "-------------------------------------------------------------------"
find kb/processes -name "*placeholder*" | wc -l | xargs echo "Count:"
find kb/processes -name "*placeholder*" | head -20

echo ""
echo "3. Recipes using import_placeholder processes:"
echo "-------------------------------------------------------------------"
grep -r "process_id: import_placeholder" kb/recipes --include="*.yaml" -l | wc -l | xargs echo "Count:"

echo ""
echo "4. Items explicitly named as placeholders:"
echo "-------------------------------------------------------------------"
find kb/items -name "*placeholder*" | wc -l | xargs echo "Count:"
find kb/items -name "*placeholder*"

echo ""
echo "5. Processes with 'placeholder' in notes (sampled):"
echo "-------------------------------------------------------------------"
grep -r "notes:.*placeholder" kb/processes --include="*.yaml" -l | wc -l | xargs echo "Count:"
grep -r "notes:.*placeholder" kb/processes --include="*.yaml" -l | head -10

echo ""
echo "==================================================================="
echo "To get full lists, run individual commands from this script"
echo "==================================================================="
