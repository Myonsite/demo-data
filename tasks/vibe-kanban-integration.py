#!/usr/bin/env python3
"""
Vibe-Kanban Integration Script for Demo Data Tasks
Converts tasks from JSON format to Vibe-Kanban board structure
"""

import json
from datetime import datetime
from pathlib import Path


def load_tasks():
    """Load tasks from JSON file."""
    with open('demo-data-tasks.json', 'r') as f:
        return json.load(f)


def create_vibe_kanban_structure():
    """Create Vibe-Kanban directory structure."""
    base_path = Path('../../kubernetes/vibe-kanban/boards/demo-data')
    
    # Create directories
    directories = [
        base_path / 'epics',
        base_path / 'tasks' / 'backlog',
        base_path / 'tasks' / 'in-progress',
        base_path / 'tasks' / 'review',
        base_path / 'tasks' / 'done',
        base_path / 'attachments',
        base_path / 'comments'
    ]
    
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)
    
    return base_path


def generate_board_config(data, base_path):
    """Generate board configuration file."""
    config = {
        "board": {
            "id": "board-demo-data",
            "name": "Demo Data Generation System",
            "description": data['description'],
            "created_at": datetime.now().isoformat(),
            "updated_at": datetime.now().isoformat(),
            "columns": [
                {
                    "id": "col-backlog",
                    "title": "Backlog",
                    "order": 0,
                    "wip_limit": None
                },
                {
                    "id": "col-in-progress",
                    "title": "In Progress",
                    "order": 1,
                    "wip_limit": 5
                },
                {
                    "id": "col-review",
                    "title": "Review",
                    "order": 2,
                    "wip_limit": 3
                },
                {
                    "id": "col-done",
                    "title": "Done",
                    "order": 3,
                    "wip_limit": None
                }
            ],
            "swimlanes": [
                {"id": "lane-critical", "title": "Critical", "order": 0},
                {"id": "lane-high", "title": "High Priority", "order": 1},
                {"id": "lane-medium", "title": "Medium Priority", "order": 2},
                {"id": "lane-low", "title": "Low Priority", "order": 3}
            ],
            "labels": [
                {"id": "label-architecture", "name": "Architecture",
                 "color": "#FF6B6B"},
                {"id": "label-generator", "name": "Generator",
                 "color": "#4ECDC4"},
                {"id": "label-validation", "name": "Validation",
                 "color": "#45B7D1"},
                {"id": "label-export", "name": "Export/Import",
                 "color": "#FFA07A"},
                {"id": "label-scenario", "name": "Scenario",
                 "color": "#98D8C8"},
                {"id": "label-performance", "name": "Performance",
                 "color": "#F7DC6F"},
                {"id": "label-testing", "name": "Testing",
                 "color": "#BB8FCE"},
                {"id": "label-documentation", "name": "Documentation",
                 "color": "#85C1E2"}
            ],
            "team_members": [
                {"id": "team-backend", "name": "Backend Team",
                 "avatar": "BE"},
                {"id": "team-frontend", "name": "Frontend Team",
                 "avatar": "FE"},
                {"id": "team-data", "name": "Data Team", "avatar": "DT"},
                {"id": "team-clinical", "name": "Clinical Team",
                 "avatar": "CL"},
                {"id": "team-qa", "name": "QA Team", "avatar": "QA"},
                {"id": "team-product", "name": "Product Team",
                 "avatar": "PD"},
                {"id": "team-integration", "name": "Integration Team",
                 "avatar": "IN"},
                {"id": "team-documentation", "name": "Documentation Team",
                 "avatar": "DC"}
            ]
        }
    }
    
    config_path = base_path / 'board-config.json'
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    return config


def create_epic_files(epics, base_path):
    """Create epic definition files."""
    epic_path = base_path / 'epics'
    
    for epic in epics:
        epic_file = {
            "epic": {
                "id": epic['id'],
                "title": epic['title'],
                "description": epic['description'],
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
                "status": "active",
                "color": "#" + epic['id'][-3:].replace('0', 'A') + "DC4",
                "progress": 0,
                "tasks": []
            }
        }
        
        file_path = epic_path / f"{epic['id']}.json"
        with open(file_path, 'w') as f:
            json.dump(epic_file, f, indent=2)


def create_task_files(tasks, base_path):
    """Create individual task files."""
    for task in tasks:
        # Determine swimlane based on priority
        swimlane_map = {
            'critical': 'lane-critical',
            'high': 'lane-high',
            'medium': 'lane-medium',
            'low': 'lane-low'
        }
        
        # Map tags to labels
        label_map = {
            'architecture': 'label-architecture',
            'generator': 'label-generator',
            'validation': 'label-validation',
            'export': 'label-export',
            'import': 'label-export',
            'scenario': 'label-scenario',
            'performance': 'label-performance',
            'testing': 'label-testing',
            'documentation': 'label-documentation'
        }
        
        task_labels = []
        for tag in task.get('tags', []):
            if tag in label_map:
                task_labels.append(label_map[tag])
        
        # Map assignee to team member
        team_map = {
            'backend-team': 'team-backend',
            'frontend-team': 'team-frontend',
            'data-team': 'team-data',
            'clinical-team': 'team-clinical',
            'qa-team': 'team-qa',
            'product-team': 'team-product',
            'integration-team': 'team-integration',
            'documentation-team': 'team-documentation'
        }
        
        task_file = {
            "task": {
                "id": task['id'],
                "title": task['title'],
                "description": task['description'],
                "epic_id": task['epic_id'],
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat(),
                "status": "backlog",
                "priority": task['priority'],
                "swimlane": swimlane_map.get(task['priority'],
                                             'lane-medium'),
                "assignee": team_map.get(task['assignee'],
                                        'team-backend'),
                "estimated_hours": task['estimated_hours'],
                "actual_hours": 0,
                "labels": task_labels,
                "dependencies": task.get('dependencies', []),
                "acceptance_criteria": task.get('acceptance_criteria', []),
                "checklist": [
                    {"id": f"check-{i}", "text": criteria,
                     "completed": False}
                    for i, criteria in enumerate(
                        task.get('acceptance_criteria', []))
                ],
                "attachments": [],
                "comments": []
            }
        }
        
        # Save to backlog initially
        file_path = base_path / 'tasks' / 'backlog' / f"{task['id']}.json"
        with open(file_path, 'w') as f:
            json.dump(task_file, f, indent=2)


def create_milestones_file(milestones, base_path):
    """Create milestones tracking file."""
    milestones_data = {
        "milestones": [
            {
                "id": milestone['id'],
                "title": milestone['title'],
                "target_date": milestone['target_date'],
                "tasks": milestone['tasks'],
                "status": "pending",
                "progress": 0,
                "created_at": datetime.now().isoformat(),
                "updated_at": datetime.now().isoformat()
            }
            for milestone in milestones
        ]
    }
    
    file_path = base_path / 'milestones.json'
    with open(file_path, 'w') as f:
        json.dump(milestones_data, f, indent=2)


def generate_summary_report(data, base_path):
    """Generate a summary report of the task breakdown."""
    total_hours = sum(task['estimated_hours'] for task in data['tasks'])
    report = f"""# Demo Data Generation System - Task Summary

Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

## Overview
- **Total Epics**: {len(data['epics'])}
- **Total Tasks**: {len(data['tasks'])}
- **Total Estimated Hours**: {total_hours}

## Epic Breakdown
"""
    
    for epic in data['epics']:
        epic_tasks = [t for t in data['tasks'] if t['epic_id'] == epic['id']]
        epic_hours = sum(t['estimated_hours'] for t in epic_tasks)
        report += f"\n### {epic['title']}"
        report += f"\n- Tasks: {len(epic_tasks)}"
        report += f"\n- Estimated Hours: {epic_hours}"
        report += f"\n- Description: {epic['description']}\n"
    
    report += "\n## Priority Distribution\n"
    priority_counts = {}
    for task in data['tasks']:
        priority = task['priority']
        priority_counts[priority] = priority_counts.get(priority, 0) + 1
    
    for priority, count in sorted(priority_counts.items()):
        report += f"- **{priority.title()}**: {count} tasks\n"
    
    report += "\n## Team Assignment\n"
    team_counts = {}
    for task in data['tasks']:
        team = task['assignee']
        team_counts[team] = team_counts.get(team, 0) + 1
    
    for team, count in sorted(team_counts.items()):
        report += f"- **{team.replace('-', ' ').title()}**: {count} tasks\n"
    
    report += "\n## Milestones\n"
    for milestone in data['milestones']:
        report += f"\n### {milestone['title']}"
        report += f"\n- Target Date: {milestone['target_date']}"
        report += f"\n- Tasks: {', '.join(milestone['tasks'])}\n"
    
    # Save report
    report_path = base_path / 'TASK_SUMMARY.md'
    with open(report_path, 'w') as f:
        f.write(report)
    
    return report


def main():
    """Main execution function."""
    print("🚀 Starting Vibe-Kanban Integration for Demo Data Tasks...")
    
    # Load tasks
    data = load_tasks()
    epics_count = len(data['epics'])
    tasks_count = len(data['tasks'])
    print(f"✅ Loaded {tasks_count} tasks across {epics_count} epics")
    
    # Create directory structure
    base_path = create_vibe_kanban_structure()
    print(f"✅ Created Vibe-Kanban structure at: {base_path}")
    
    # Generate board configuration
    generate_board_config(data, base_path)
    print("✅ Generated board configuration")
    
    # Create epic files
    create_epic_files(data['epics'], base_path)
    print(f"✅ Created {len(data['epics'])} epic files")
    
    # Create task files
    create_task_files(data['tasks'], base_path)
    print(f"✅ Created {len(data['tasks'])} task files")
    
    # Create milestones file
    create_milestones_file(data['milestones'], base_path)
    print(f"✅ Created milestones tracking file")
    
    # Generate summary report
    generate_summary_report(data, base_path)
    print("✅ Generated task summary report")
    
    print("\n✨ Vibe-Kanban integration complete!")
    print(f"📁 Board location: {base_path}")
    print("\nNext steps:")
    print("1. Review the generated board configuration")
    print("2. Import tasks into your Vibe-Kanban instance")
    print("3. Assign team members to tasks")
    print("4. Start development!")


if __name__ == "__main__":
    main() 