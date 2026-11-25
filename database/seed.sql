-- Insert samples records.

INSERT INTO public_documents (title, content)
VALUES
    ('Project Overview', 'This is public project information.'),
    ('General Information', 'This document is publicly accessible.')
ON CONFLICT (title) DO NOTHING;


INSERT INTO private_documents (owner_id, title, content)
VALUES
    ('user_1', 'Personal Notes', 'Private information belonging to user 1.'),
    ('user_2', 'Personal Notes', 'Private information belonging to user 2.')
ON CONFLICT (owner_id, title) DO NOTHING;